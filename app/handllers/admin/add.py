import asyncio
from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message

from app.filters.is_admin import IsAdmin

from app.DataBase.models import Item
from app.DataBase.models import async_session

add_router = Router()


class AddItemStates(StatesGroup):
    name = State()
    price = State()
    description = State()
    code = State()
    amount = State()
    size = State()
    gender = State()
    photo = State()  # для фото можно ожидать ссылку или загружать файл


@add_router.callback_query(IsAdmin(), F.data == "add_item")
async def start_add_item(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Введите название товара:")
    await state.set_state(AddItemStates.name)
    await callback.answer()
    
    
@add_router.message(AddItemStates.name, IsAdmin())
async def process_name(message: Message, state: FSMContext):
    name = message.text
    if len(name) > 25:  # ограничение модели String(25)
        await message.answer("Название слишком длинное (макс. 25 символов). Попробуйте снова:")
        return
    await state.update_data(name=name)
    await message.answer("Введите цену товара (только число):")
    await state.set_state(AddItemStates.price)
    
    
@add_router.message(AddItemStates.price, IsAdmin())
async def process_price(message: Message, state: FSMContext):
    try:
        price = int(message.text)
    except ValueError:
        await message.answer("Цена должна быть числом. Попробуйте снова:")
        return
    await state.update_data(price=price)
    await message.answer("Введите описание товара:")
    await state.set_state(AddItemStates.description)
    
    
@add_router.message(AddItemStates.description, IsAdmin())
async def process_description(message: Message, state: FSMContext):
    description = message.text
    if len(description) > 100:  # ограничение модели String(100)
        await message.answer("Описание слишком длинное (макс. 100 символов). Попробуйте снова:")
        return
    await state.update_data(description=description)
    await message.answer("Введите код товара (строка):")
    await state.set_state(AddItemStates.code)


@add_router.message(AddItemStates.amount, IsAdmin())
async def process_amount(message: Message, state: FSMContext):
    try:
        amount = int(message.text)
    except ValueError:
        await message.answer("Количество должно быть числом. Повторите:")
        return
    await state.update_data(amount=amount)
    await message.answer("Введите размер (или пропустите, отправив '-'):")
    await state.set_state(AddItemStates.size)

@add_router.message(AddItemStates.size, IsAdmin())
async def process_size(message: Message, state: FSMContext):
    size = message.text if message.text != '-' else ''
    await state.update_data(size=size)
    await message.answer("Введите гендер (или пропустите, отправив '-'):")
    await state.set_state(AddItemStates.gender)

@add_router.message(AddItemStates.gender, IsAdmin())
async def process_gender(message: Message, state: FSMContext):
    gender = message.text if message.text != '-' else ''
    await state.update_data(gender=gender)
    # Можно запросить фото или сразу сохранить
    await message.answer("Отправьте ссылку на фото товара:")
    await state.set_state(AddItemStates.photo)

@add_router.message(AddItemStates.photo, IsAdmin())
async def process_photo(message: Message, state: FSMContext):
    photo_url = message.text
    # Здесь можно добавить проверку, что это валидная ссылка
    await state.update_data(photo_url=photo_url)

    data = await state.get_data()
    # Создаём товар со всеми полями
    new_item = Item(
        name=data['name'],
        price=data['price'],
        description=data['description'],
        item_id=data['code'],
        photo_url=data.get('photo_url', ''),
        amount=data.get('amount', 0),
        size=data.get('size', ''),
        gender=data.get('gender', '')
    )

    async with async_session() as session:
        session.add(new_item)
        await session.commit()

    await message.answer(f"Товар «{data['name']}» успешно добавлен!")
    await state.clear()
    

    