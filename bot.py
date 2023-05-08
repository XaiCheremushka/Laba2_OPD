import time

from aiogram import Bot, Dispatcher, executor, types
from config import token, commands
from parsing import parse


bot = Bot(token)
dp = Dispatcher(bot)

def fileWork(mod, str="", poz=0):
    if mod == 'w':
        list = []
        with open('data.txt', 'r') as f:
            list = f.read().split("\n")
            list[poz] = str
        with open('data.txt', 'w') as f:
            for i in list:
                f.write(i+"\n")
    elif mod == 'r':
        with open('data.txt', 'r') as f:
            return f.readlines()

def num_after_point(s):
    if not '.' in s:
        return 0
    return len(s) - s.index('.') - 1


@dp.message_handler(commands='start')
async def start(message: types.Message):
    with open('data.txt', 'w') as f:
        f.write("0\n0")
    await message.answer(text="Привет! Я бот, который поможет тебе не потерять все деньги на бирже! Вот мои возможности: " + commands)

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.answer(text=commands)

@dp.message_handler(commands='checkRate')
async def checkRate(message: types.Message):
    await message.answer(text=parse())

@dp.message_handler(commands='setHighLimit')
async def setHighLimit(message: types.Message):
    arg = message.text[14:]
    if ('.' in arg) and (num_after_point(arg) == 3): # Проверяем количество знаков после запятой
        fileWork('w', arg, 0)
        await message.answer(text='Верхний предел установлен!')
    else:
        await message.answer(text='Вы неправильно ввели число! Пожалуйста, соблюдайте формат записи! '
                                  '(формат записи: "/setHighLimit 65.125")')

@dp.message_handler(commands='setLowLimit')
async def setLowLimit(message: types.Message):
    arg = message.text[13:]
    if ('.' in arg) and (num_after_point(arg) == 3):  # Проверяем количество знаков после запятой
        fileWork('w', arg, 1)
        await message.answer(text='Нижний предел установлен!')
    else:
        await message.answer(text='Вы неправильно ввели число! Пожалуйста, соблюдайте формат записи! '
                                  '(формат записи: "/setLowLimit 65.125")')

@dp.message_handler(commands='startWork')
async def startWork(message: types.Message):
    bounds = fileWork('r')
    print(bounds)
    if bounds[0] == '0' and bounds[1] == '0':
        await message.answer(text='Установите пределы перед запуском!')
    else:
        await message.answer(text=f'Бот запущен! Пределы: верхний - {bounds[0]}, нижний - {bounds[1]} \n Ждите сообщений.')
        while True:
            if float(parse()) > float(bounds[0]):
                await message.answer(text=f'Цена превысила верхний предел! Текущий курс: {parse()}')
                break
            elif float(parse()) < float(bounds[1]):
                await message.answer(text=f'Цена превысила нижний предел! Текущий курс: {parse()}')
                break
            else:
                time.sleep(30)




def run():
    executor.start_polling(dp)





# @dp.message_handler(commands='setNewLimits')
# async def setNewLimits(message: types.Message):
#     await message.answer(text='Введите верхний предел:')
#     @dp.message_handler()
#     async def highLim(message: types.Message):
#         bounds[0] = message.text
#         await message.answer(text='Введите нижний предел:')
#     @dp.message_handler()
#     async def lowLim(message: types.Message):
#         bounds[1] = message.text
#         await message.answer(text='Данные введены!')
#
#     print(bounds)


# @dp.message_handler()
# async def setLimits(message: types.Message):
