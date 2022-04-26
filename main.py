import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

wikipedia.set_lang('uz')

API_TOKEN = '5208297006:AAHlSQXHNc2307sbkPnmis_1G66SPTtu-4A'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hello and welcome to Wikipedia bot!")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    try:
        response = wikipedia.summary(message.text)
        await message.answer(response)
    except:
        await message.answer("No such information was found")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
