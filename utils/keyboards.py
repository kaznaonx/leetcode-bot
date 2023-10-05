from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton

main = ReplyKeyboardMarkup (
    keyboard=[
        [
            KeyboardButton(text='Profile'),
            KeyboardButton(text='Problems'),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Select a button for action'
)

def problem_link(slug: str):
    links = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Link on problem', url=f'https://leetcode.com/problems/{slug}'),
            ]
        ]
    )

    return links