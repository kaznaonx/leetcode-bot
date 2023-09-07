from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from dotenv import load_dotenv
import os

load_dotenv('utils/.env')
LEETCODE_PROBLEMS = os.getenv('LEETCODE_PROBLEMS')

main_kbrd = [
    [KeyboardButton(text='Profile'),
    KeyboardButton(text='Problems')]
]

kbrd = ReplyKeyboardMarkup(keyboard=main_kbrd, resize_keyboard=True, input_field_placeholder='Select button below')

def problem_link(slug: str):
    return InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Link on problem', url=f'{LEETCODE_PROBLEMS}{slug}'))