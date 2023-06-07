import asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types
import logging

TOKEN='6221978203:AAHx4KrgZOg6Ug9IFk2EByL-qIawcSvPDzQ'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
#kirill = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ .,():;1234567890+-=')
#spam = ('κᴩπᴀρᧉτ')
flage = 0


'''@dp.message_handler()
async def main_menu_button(message: types.Message):
    spam_am = 0
    kiros = 0
    lend = len(message.text)
    for i in message.text:
        if i in spam:
            spam_am += 1
        if i in kirill:
            kiros += 1
    print(spam_am, lend, kiros)
    if kiros / lend < 0.95 and spam_am > 2 or spam_am > 5:
        await bot.send_message(chat_id=config.ADMIN_CHAT_ID,
                               text=(str(message.chat.id) + ' ' + str(message.chat.title) + ' ' + message.text))
        await bot.delete_message(message.chat.id, message.message_id)'''


@dp.message_handler(commands="time")
async def time_mim(message: types.Message):
    global flage
    print(flage)
    if flage == 0:
        flage = 1
        while True:
            await asyncio.sleep(1)
            now = datetime.now()
            current_time = now.strftime("%w %H:%M:%S")
            print(current_time)
            if current_time == '4 18:55:00':
                await bot.send_message(message.chat.id, 'Time to pay money!')
                print('was')
    else:
        await bot.delete_message(message.chat.id, message.message_id)
        await bot.send_message(message.chat.id, text = 'You have already launched the function')
        await asyncio.sleep(3)
        await bot.delete_message(message.chat.id, message.message_id+1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
