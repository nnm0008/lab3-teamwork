from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token="ВАШ_ТОКЕН_БОТА")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Создаем кнопки меню
    keyboard = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton("Информация", callback_data="info")
    btn2 = InlineKeyboardButton("Помощь", callback_data="help")
    keyboard.add(btn1, btn2)

    await message.answer("Привет! Выбери нужный пункт меню:", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data)
async def process_callback(callback_query: types.CallbackQuery):
    # Обработка нажатий на кнопки
    if callback_query.data == "info":
        await bot.send_message(callback_query.from_user.id, "Это раздел с информацией.")
    elif callback_query.data == "help":
        await bot.send_message(callback_query.from_user.id, "Это раздел помощи.")
    
    await bot.answer_callback_query(callback_query.id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
