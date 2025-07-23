import asyncio
from aiogram import Bot, Dispatcher
from data.config import TOKEN
from handlers.start import router as start_router
from handlers.profile import router as profile_router

async def main():
    bot = Bot(token="8072375183:AAGKJxNfXsbjboudiEwiAItaO8hCx7gNes4")  # ✅ Ваш реальный токен
    dp = Dispatcher()
    
    # Подключаем роутеры
    dp.include_router(start_router)
    dp.include_router(profile_router)
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())