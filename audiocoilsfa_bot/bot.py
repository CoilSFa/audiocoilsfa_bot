
import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from utils.audio_handler import process_audio
from utils.auth import is_authorized

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=types.ContentType.VOICE | types.ContentType.AUDIO | types.ContentType.DOCUMENT)
async def handle_audio(message: types.Message):
    if not is_authorized(message.from_user.id):
        await message.answer("⛔ У вас нет доступа. Введите ключ.")
        return

    await message.reply("🔊 Обрабатываю аудио...")
    result = await process_audio(message)
    await message.answer(result["text"])
    await message.answer_document(result["pdf"])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
