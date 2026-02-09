from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Профиль", callback_data="profile"), InlineKeyboardButton(text="Каталог", callback_data="catalog"))
    return builder.as_markup()



def get_catalog():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="", callback_data="shoose"))
    return builder.as_markup()