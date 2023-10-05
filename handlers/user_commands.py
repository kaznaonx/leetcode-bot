from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from utils import keyboards

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'''
Hi, {message.from_user.username}
This is a Telegram Bot to view LeetCode statistics of your profile and randomly select a problem''', reply_markup=keyboards.main)