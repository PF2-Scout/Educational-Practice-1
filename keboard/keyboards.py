from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard= True)
    button_1 = KeyboardButton('Отправь фото кота')
    button_2 = KeyboardButton('Перейти на вторую клавиатуру')
    button_3 = KeyboardButton('Перейти на третью клавиатуру')
    button_4 = KeyboardButton('Перейти на четвёртую клавиатуру')
    keyboard.add(button_1, button_2, button_3, button_4)
    return keyboard

def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard= True)
    button_5 = KeyboardButton ('Отправь фото собаки')
    button_6 = KeyboardButton ('Вернуться на 1 клавиатуру')
    keyboard_2.add(button_5, button_6)
    return keyboard_2

def get_keyboard_3():
    keyboard_3 = ReplyKeyboardMarkup(resize_keyboard= True)
    button_7 = KeyboardButton ('Отправь фото Максвелла')
    button_8 = KeyboardButton ('Вернуться на 1 клавиатуру')
    keyboard_3.add(button_7, button_8)
    return keyboard_3

def get_keyboard_4():
    keyboard_4 = ReplyKeyboardMarkup(resize_keyboard= True)
    button_9 = KeyboardButton ('Отправь фото Шлёппы')
    button_10 = KeyboardButton ('Вернуться на 1 клавиатуру')
    keyboard_4.add(button_9, button_10)
    return keyboard_4