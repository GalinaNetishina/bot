import subprocess

from aiogram import Router
from aiogram.types import Message

router = Router()
@router.message()
async def send_answer(message: Message):
    user_id = message.from_user.id
    answer = subprocess.run(["python", "-c", message.text], capture_output=True, text=True).stdout

    await message.answer(text=answer or "Не смог(")
