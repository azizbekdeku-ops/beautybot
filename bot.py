import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import os
TOKEN = os.getenv("BOT_TOKEN")


router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [KeyboardButton(text="💇 Услуги"), KeyboardButton(text="📅 Записаться")],
            [KeyboardButton(text="📞 Контакты")]
        ]
    )
    await message.answer("Привет! Я бот салона красоты 💅\nВыберите действие:", reply_markup=kb)

@router.message(lambda m: m.text == "💇 Услуги")
async def services(message: types.Message):
    await message.answer("Наши услуги:\n— Маникюр 💅\n— Стрижка 💇‍♀️\n— Окрашивание 💆‍♀️")

@router.message(lambda m: m.text == "📅 Записаться")
async def book(message: types.Message):
    await message.answer("Чтобы записаться, напишите дату и время. Мы свяжемся с вами!")

@router.message(lambda m: m.text == "📞 Контакты")
async def contacts(message: types.Message):
    await message.answer("📍 Москва, ул. Цветочная 5\n📞 +7 (900) 000-00-00")

async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
