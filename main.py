import asyncio
import os
from dotenv import load_dotenv
from aiogram import Dispatcher, types, Bot, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command


dp = Dispatcher()

@dp.message(Command("start"))
async def menu_start(message: types.Message):
    kb = [
        [
            types.InlineKeyboardButton(text='Д/З', callback_data='Homework'),
            types.InlineKeyboardButton(text='Очередь', callback_data='queue')
        ],
        [
            types.InlineKeyboardButton(text='Расписание', callback_data='Schedule'),
            types.InlineKeyboardButton(text='Опросы', url='https://t.me/c/2956229692/521')
        ],
        [
            types.InlineKeyboardButton(text='Важная информ.', callback_data='info'),
            types.InlineKeyboardButton(text='Ссылки на беседы групп', callback_data='lincs'),
        ]
    ]

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)

    await message.answer(
        'Привет, друг!\nЭтот бот поможет тебе в учебе\n\n<i>С чем конкретно тебе помочь?</i>',
        reply_markup=keyboard
    )

@dp.callback_query(F.data == 'menu')
async def menu(query: types.CallbackQuery):
    kb = [
        [
            types.InlineKeyboardButton(text='Д/З', callback_data='Homework'),
            types.InlineKeyboardButton(text='Очередь', callback_data='queue')
        ],
        [
            types.InlineKeyboardButton(text='Расписание', callback_data='Schedule'),
            types.InlineKeyboardButton(text='Опросы', url='https://t.me/c/2956229692/521')
        ],
        [
            types.InlineKeyboardButton(text='Важная информ.', callback_data='info')
        ]
    ]

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)

    await query.message.edit_text(
        '<i>С чем конкретно тебе помочь?</i>',
        reply_markup=keyboard
    )

@dp.callback_query(F.data == 'menu_dop')
async def menu_dop(query: types.CallbackQuery):
    kb = [
        [
            types.InlineKeyboardButton(text='Д/З', callback_data='Homework'),
            types.InlineKeyboardButton(text='Очередь', callback_data='queue')
        ],
        [
            types.InlineKeyboardButton(text='Расписание', callback_data='Schedule'),
            types.InlineKeyboardButton(text='Опросы', url='https://t.me/c/2956229692/521')
        ],
        [
            types.InlineKeyboardButton(text='Важная информ.', callback_data='info')
        ]
    ]
    await query.message.edit_reply_markup(reply_markup=None)
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await query.answer('Выберите дополнителный параметр')
    await query.message.answer(
        '<i>С чем конкретно тебе помочь?</i>',
        reply_markup=keyboard
    )

@dp.callback_query(F.data == 'Homework')
async def homework(callback: types.CallbackQuery):
    kb = [[types.InlineKeyboardButton(text='Вернуться к меню', callback_data='menu'),
           types.InlineKeyboardButton(text='Узнать дополнительно', callback_data='menu_dop')]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.answer("Раздел ДЗ")
    await callback.message.edit_text("Тут будет домашка", reply_markup=keyboard)



async def main():
    load_dotenv()
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    # BOT_TOKEN = os.environ.get("BOT_TOKEN")
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN не найден")
    else:
        bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())