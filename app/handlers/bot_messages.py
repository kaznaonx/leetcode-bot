from aiogram import Router, F
from aiogram.types import Message

from app.utils.requests_random_problem import get_problem_info
from app.utils.requests_user_info import get_user_info
from app.utils import keyboards
from . import messages

router = Router()

@router.message(F.text == 'Profile')
async def profile(message: Message):
    await message.answer(f'Enter LeetCode Nick')

    @router.message(F.text)
    async def show_profile_info(message: Message):
        nick = message.text
        profile_info = get_user_info(nick)

        if isinstance(profile_info, str):
            await message.answer(profile_info)
        else:
            await message.answer(messages.profile_info(nick, profile_info))

@router.message(F.text == 'Problems')
async def show_random_problem(message: Message):
    problem_info = get_problem_info()

    await message.answer(
        messages.problem_info(problem_info),
        reply_markup=keyboards.problem_link(problem_info['problem_title_slug'])
    )