from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📦 Профиль"), KeyboardButton(text="💱 Курс юаня")],
        [KeyboardButton(text="🚚 Рассчитать доставку")]
    ],
    resize_keyboard=True
)

# Меню профиля
profile_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📋 Мои заказы", callback_data="orders"),
         InlineKeyboardButton(text="⭐ Избранное", callback_data="favorites")],
        [InlineKeyboardButton(text="💰 Баланс", callback_data="balance")]
    ]
)