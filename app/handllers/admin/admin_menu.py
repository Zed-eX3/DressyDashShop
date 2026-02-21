from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_admin_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
                    text="Каталог", callback_data="catalog"
                                                                        ),
                InlineKeyboardButton(
                    text="Профиль", callback_data="profile"
                                                                       ))
    builder.row(
        InlineKeyboardButton(
            text='Отзывы', callback_data='feedback'
        ))
    builder.row(
        InlineKeyboardButton(
            text='Тех поддержка', callback_data='feedback'
        ))
    builder.row(
        InlineKeyboardButton(
            text='Добавить товар', callback_data='add'
        ))
    
    return builder.as_markup()
