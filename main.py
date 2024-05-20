from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard= True)
button_1 = KeyboardButton ('Отправь фото кота')
button_2 = KeyboardButton ('Перейти на следующую клавиатуру')
keyboard.add(button_1, button_2)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start', description= 'Команда для запуска бота'),
        types.BotCommand(command='/help', description='Команда для запуска меню бота')
    ]

    await bot.set_my_commands(commands)


@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('Привет, я твой первый ЭХО бот', reply_markup= keyboard)

@dp.message_handler(lambda message: message.text == 'Отправь фото кота')
async def button_1_click(message:  types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://www.purina.co.uk/sites/default/files/styles/ttt_image_510/public/2020-12/Understanding%20Your%20Cat%27s%20Body%20LanguageHERO.jpg?itok=soc9Ieol', caption= 'Вот тебе кот!' )

@dp.message_handler(lambda message: message.text == 'Кнопка 2')
async def button_2_click(message:  types.Message):
    await message.answer('Ты нажал кнопку 2')

@dp.message_handler(commands= 'help')
async def help(message: types.Message):
    await message.reply('Я могу помочь тебе с .....')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)
