from aiogram import Bot, Dispatcher, executor, types
from config import token, commands
from parsing import parse
from aiogram.Dispetcher.Filters import Command

bot = Bot(token)
dp = Dispatcher(bot)

highLimit = ''
lowLimit = ''

def num_after_point(s):
    if not '.' in s:
        return 0
    return len(s) - s.index('.') - 1

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(text="Привет! Я бот, который поможет тебе не потерять все деньги на бирже!")
    await message.answer(text=commands)

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.answer(text=commands)

@dp.message_handler(commands='checkRate')
async def checkRate(message: types.Message):
    await message.answer(text=parse())

@dp.message_handler(commands='setHighLimit')
async def setHighLimit(message: types.Message, command: CommandObject):
    arg = command.args
    if (',' in arg) and (num_after_point(arg.replace(',', '.')) == 3): # Проверяем количество знаков после запятой
        highLimit = message.text
        await message.answer(text='Верхний предел установлен!')
    else:
        await message.answer(text='Вы неправильно ввели число! Пожалуйста, соблюдайте формат записи! '
                                  '(формат записи: "/setHighLimit 65,125")')

@dp.message_handler(commands='setLowLimit')
async def setLowLimit(message: types.Message, command: CommandObject):
    arg = command.args
    if (',' in arg) and (num_after_point(arg.replace(',', '.')) == 3):  # Проверяем количество знаков после запятой
        lowLimit = message.text
        await message.answer(text='Нижний предел установлен!')
    else:
        await message.answer(text='Вы неправильно ввели число! Пожалуйста, соблюдайте формат записи! '
                                  '(формат записи: "/setLowLimit 65,125")')




# @dp.message_handler()
# async def setLimits(message: types.Message):


