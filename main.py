from aiogram import executor
import bot

if __name__ == '__main__':
    executor.start_polling(bot.dp)
    print(bot.highLimit)
