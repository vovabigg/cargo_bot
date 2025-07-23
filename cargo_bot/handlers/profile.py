from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from keyboards.menu import profile_menu

router = Router()

@router.message(F.text == "📦 Профиль")
async def profile_command(message: Message):
    await message.answer("📦 Ваш профиль:", reply_markup=profile_menu)

@router.callback_query(F.data.in_(["orders", "favorites", "balance"]))
async def profile_callback(callback: CallbackQuery):
    if callback.data == "orders":
        await callback.message.edit_text("📋 Ваши заказы:\nПока здесь пусто. Хотите оформить новый заказ?")
    elif callback.data == "favorites":
        await callback.message.edit_text("⭐ Избранное:\nВы ещё ничего не добавили в избранное.")
    elif callback.data == "balance":
        await callback.message.edit_text("💰 Ваш баланс: 0 ₽\nПополнить баланс можно в разделе оплаты.")
    await callback.answer()