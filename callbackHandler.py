from aiogram import F, Router
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup
from aiogram.filters.command import Command

callback = Router()

@callback.callback_query(F.data == "trainings")
async def handle_trainings(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="💪 Тренировки для женщин", callback_data="trainings of woman")
            ],
            [
                InlineKeyboardButton(text="💪 Тренировки для мужчин" , callback_data="trainings of man")
            ]
        ]
    )
    await callback.message.edit_text("Вы выбрали тренировки", reply_markup=keyboard)
    await callback.answer()


