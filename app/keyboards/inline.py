from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_menu():
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
    
    return builder.as_markup()


def get_catalog():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='Красовки', callback_data='sneakers'
        ))
    builder.row(
        InlineKeyboardButton(
            text='Штаны', callback_data='pants'
        ))
    builder.row(
         InlineKeyboardButton(
            text='Техника', callback_data='tech'
        ))
    builder.row(
         InlineKeyboardButton(
            text='назад', callback_data='start'
        ))
    return builder.as_markup()



def comeback_to_menu():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='Вернуться в меню', callback_data='start'
        ))
    return builder.as_markup()