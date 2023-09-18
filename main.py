from dotenv import load_dotenv
from os import getenv

load_dotenv()
TOKEN = getenv('VK_BOT_TOKEN')
print(TOKEN)

# Example of sending and receiving an event after pressing the Callback button
# Documentation: https://dev.vk.com/api/bots/development/keyboard#Callback-кнопки
import logging
import os

from vkbottle import Callback, GroupEventType, Keyboard
from vkbottle.bot import Bot, Message, MessageEvent, rules

# Load token from system environment variable
# https://12factor.net/config
bot = Bot(TOKEN)

logging.basicConfig(level=logging.INFO)


@bot.on.private_message()
async def hi_handler(message: Message):
    users_info = await bot.api.users.get(message.from_id)
    await message.answer("Привет, {}".format(users_info[0].first_name))

bot.run_forever()


