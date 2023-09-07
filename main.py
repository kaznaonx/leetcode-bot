from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

from utils.random_problem import get_problem_info
from utils.user_info import get_user_info

import utils.keyboards as kbrd

load_dotenv('utils/.env')
TOKEN = os.getenv('TOKEN')
LEETCODE_DOMAIN = os.getenv('LEETCODE_DOMAIN')

bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['Start'])
async def main_menu(message: types.Message):
    await message.answer(f'''
Hi, {message.from_user.mention}
This is a Telegram Bot to view LeetCode statistics of your profile and randomly select a problem''', reply_markup=kbrd.kbrd)

@dp.message_handler(text='Profile')
async def user_profile(message: types.Message):
    await message.answer(f'Еnter your LeetCode nickname')

    @dp.message_handler(lambda message: message.text)
    async def user_nick_input(message: types.Message):
        NICKNAME = message.text
        user_info = get_user_info(NICKNAME)

        if isinstance(user_info, str):
            await message.answer(f'{user_info}', parse_mode=types.ParseMode.HTML)
        else:
            await message.answer(f'''
LeetCode profile: <a href='{LEETCODE_DOMAIN}/{NICKNAME}'>{NICKNAME}</a>

<b>Solved Problems:</b>
Easy: <b>{user_info['total_easy_problems_solved']}</b>/{user_info['total_easy_problems']}
Medium: <b>{user_info['total_medium_problems_solved']}</b>/{user_info['total_medium_problems']}
Hard: <b>{user_info['total_hard_problems_solved']}</b>/{user_info['total_hard_problems']}
Total: <b>{user_info['total_problems_solved']}</b>/{user_info['total_problems']}

<b>{user_info['submissions_last_year']}</b> submissions in the last year

Rank: <b>{user_info['user_rank']}</b>
Reputation: <b>{user_info['reputation']}</b>

Contribution Point: <b>{user_info['contribution_point']}</b>''', parse_mode=types.ParseMode.HTML)

@dp.message_handler(text='Problems')
async def random_problem(message: types.Message):
    problem_info = get_problem_info()
    problem_link = kbrd.problem_link(problem_info['problem_title_slug'])

    await message.answer(f'''
<b>{problem_info['problem_id']}.</b> {problem_info['problem_title']}
<b>Topic:</b> {problem_info['problem_topic']}

<b>Difficulty:</b> {problem_info['problem_difficulty']}
<b>Status:</b> {problem_info['problem_paid_only']}

Accepted <b>{problem_info['accepted']}</b> | Submissions <b>{problem_info['submissions']}</b> | Acceptance Rate <b>{problem_info['acceptance_rate']}</b>''', reply_markup=problem_link, parse_mode=types.ParseMode.HTML)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)