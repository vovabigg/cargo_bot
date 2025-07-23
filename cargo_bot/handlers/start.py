from aiogram import Router, F
from aiogram.types import Message
from keyboards.menu import menu

router = Router()

@router.message(F.command == "start")
async def start_command(message: Message):
    await message.answer_photo(
        photo="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Cargo_ship_icon.png/240px-Cargo_ship_icon.png",
        caption="👋 Добро пожаловать в сервис доставки из Китая!\n\nВыберите действие ниже:",
        reply_markup=menu
    )