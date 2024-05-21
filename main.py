from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keboard.keyboards import get_keyboard_1, get_keyboard_2

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)



async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда для запуска бота'),
        types.BotCommand(command='/help', description='Команда для запуска меню бота'),
        types.BotCommand(command='/about', description='Команда для объяснения бота')
    ]

    await bot.set_my_commands(commands)


@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('Привет, я твой первый ЭХО бот', reply_markup= get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Отправь фото кота')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://www.purina.co.uk/sites/default/files/styles/ttt_image_510/public/2020-12/Understanding%20Your%20Cat%27s%20Body%20LanguageHERO.jpg?itok=soc9Ieol', caption= 'Вот тебе кот!' )

@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут можно запросить фото собаки', reply_markup= get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Отправь фото собаки')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://www.purina.co.nz/sites/default/files/2020-12/Dog_1098119012_Teaser.jpg', caption= 'Вот тебе собака!' )

@dp.message_handler(lambda message: message.text == 'Вернуться на 1 клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут можно запросить фото кота', reply_markup= get_keyboard_1())

@dp.message_handler(commands= 'help')
async def help(message: types.Message):
    await message.reply('Я могу помочь тебе с .....')

@dp.message_handler(commands= 'about')
async def about(message: types.message):
    await message.reply('Этот бот создан для учебной практики')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)