import logging
import requests
import datetime
from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup
#---------------------------------------------------------
weather_token = "6e8d79779a0c362f14c60a1c7f363e29"
API_TOKEN = "6070338924:AAGkKJFEhkHduhozsBtCNjSwUZKb_TJwDNo"
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start',])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Привіт\nТримай інші посилання:\n@Miky667_bot\nhttps://t.me/woBotu\n")

@dp.message_handler()
async def send_iii(message: types.Message):
    if message.text == 'Иииииииииииииии':
        await message.answer('хехе')

    elif message.text == 'Привіт':
        await message.answer('І тобі привіт')
    elif message.text == 'як справи?':
        await message.answer('все добре')
    elif message.text == 'чим займаєшся?':
        await message.answer('Дивлюся анімешку та спілкуюся з тобою')
    elif message.text == 'у чому сенс твого життя?':
        await message.answer('Я робот и у меня нету смысла жизни')
    elif message.text == 'навіщо ти був створений?':
        await message.answer('щоб допомогти тобі та іншим')
    elif message.text == 'навіщо ти був створений?':
        await message.answer('щоб допомогти тобі та іншим')
    elif message.text == 'у тебе є друзі?':
        await message.answer('Мій творець та мої помічники')
    elif message.text == 'хто твій творець?':
        await message.answer('@WORLDEND98786L')
    elif message.text == '@WORLDEND98786L':
        await message.answer('це мій творець)')
    elif message.text == 'хто твій помічник?':
        await message.answer('https://t.me/Miky667_bot')

    elif message.text == 'твій тг канал': #где будут показываться новоллы и новые тг боты(подпишись)
        await message.answer('https://t.me/woBotu')
    elif message.text == 'твій тг канал?': #где будут показываться новоллы и новые тг боты(подпишись)
        await message.answer('https://t.me/woBotu')
    elif message.text == 'твій телеграм канал': #где будут показываться новоллы и новые тг боты(подпишись)
        await message.answer('https://t.me/woBotu')
    elif message.text == 'твій телеграм канал?': #где будут показываться новоллы и новые тг боты(подпишись)
        await message.answer('https://t.me/woBotu')
    elif message.text == 'https://t.me/woBotu': #подпишись 
        await message.answer('це мій тг канал')
        await message.answer('подпишись)')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
