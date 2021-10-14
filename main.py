from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from prayerTime import todaytime, tomorrowtime
from newLine import newline

bot = Bot(token="TOKEN")
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def send_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Bugungi vaqtlar", "Ertangi vaqtlar"]
    keyboard.add(*buttons)
    await message.answer("Assalomu aleykum!\n"
                         "@Masjid_robot ga xush kelibsiz!\n"
                         "Bot orqali Toshkent shahridagi namoz vaqtlarini bilishingiz mumkin!", reply_markup=keyboard)



@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("@masjid_robot boti orqali Toshkent shahridagi namoz vaqtlarini bilib olishingiz mumkin!\n"
                        "\nAloqa uchun: @sohibjaynarov")


@dp.message_handler(lambda message: message.text == "Bugungi vaqtlar")
async def without_puree(message: types.Message):
    time_dict = todaytime()
    text = newline(time_dict)
    await message.reply(text)

@dp.message_handler(lambda message: message.text == "Ertangi vaqtlar")
async def without_puree(message: types.Message):
    time_dict = tomorrowtime()
    text = newline(time_dict)
    await message.reply(text)


if __name__ == '__main__':
    executor.start_polling(dp)
