
import os
import uuid
from pydub import AudioSegment
from whisper import transcribe
from utils.summarizer import summarize_text
from utils.pdf_export import export_to_pdf

async def process_audio(message):
    file = await message.bot.get_file(message.voice.file_id if message.voice else message.document.file_id)
    file_path = file.file_path
    file_name = f"/mnt/data/{uuid.uuid4()}.mp3"
    await message.bot.download_file(file_path, file_name)

    audio = AudioSegment.from_file(file_name)
    audio.export(file_name, format="mp3")

    text = transcribe(file_name)
    summary = summarize_text(text)
    pdf_path = export_to_pdf(text)

    return {"text": summary, "pdf": open(pdf_path, "rb")}
