from aiogram import F, Router
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters.command import Command

user = Router()



@user.message (Command("start"))
async def cmd_start(message: types.Message) :
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="💪 Тренировки", callback_data="trainings"),
                InlineKeyboardButton(text="🍎 Питание", callback_data="nutrition")
            ],
            [
                InlineKeyboardButton(text="📝 Указать информацию о себе", callback_data="set_info")
            ]
        ]
    )
    await message.answer(
        "Привет! Я бот для тренировок. С чего начнем? =)",
        reply_markup=keyboard
    )

def get_goals_keyboard():
    """Клавиатура для выбора цели"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🏋️ Набор массы", callback_data="goal_mass"),
                InlineKeyboardButton(text="🔥 Похудение", callback_data="goal_weight_loss")
            ],
            [
                InlineKeyboardButton(text="💪 Поддержание формы", callback_data="goal_maintain")
            ]
        ]
    )
    return keyboard

@user.message (Command("help"))
async def cmd_help(message: types.Message) :
    await message. answer ("Бот для помощи в тренировках")
    
@user.message (Command("info"))
async def cmd_info(message: types.Message) :
    await message. answer ("Создатель круглик бублик")

