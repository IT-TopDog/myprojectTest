# from aiogram import Bot, Dispatcher 
from aiogram.types import Message 
from aiogram.utils import executor 
# from config import TOKEN
from database.db_file import Database 
from keyboards.kb import get_keyboard
from handlers.states import Registration
from bot import bot, dp


# bot = Bot(token= TOKEN)
# dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_command(message: Message):
    db = Database()
    db.connect()
    db.create_user_table()
    user_id = message.from_user.id
    check_user = db.check_user(user_id)
    if check_user:
        await message.answer('Привет, ты зарегистрирован', reply_markup=get_keyboard('start_menu'))
    else:
        registration = Registration(message)
        await registration.registration_users(message)
    
    db.close()


@dp.message_handler(text='Товары')
async def products_handler(message: Message):
    pass


@dp.message_handler(text='Корзина')
async def cart_handler(message: Message):
    pass


@dp.message_handler(text='Личный кабинет')
async def private_office_handler(message: Message):
    pass


@dp.message_handler(text='Отдел заботы')
async def support_handler(message: Message):
    pass


if __name__ =='__main__':
    executor.start_polling(dp,skip_updates=True)
