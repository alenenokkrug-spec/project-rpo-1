from aiogram import F, Router
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from aiogram.filters.command import Command

trainings = Router()

@trainings.callback_query(F.data == "trainings")
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
    await callback.message.edit_text("Выберите для кого тренировки", reply_markup=keyboard)
    await callback.answer()


@trainings.callback_query(F.data == "trainings of woman")
async def handle_trainingsofwoman(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Разминка", callback_data="Warm-up woman")
            ],
            [
                InlineKeyboardButton(text="Ноги", callback_data="Legs woman")
            ],
            [
                InlineKeyboardButton(text="Ягодицы", callback_data="Guttocks woman")
            ],
            [
                InlineKeyboardButton(text="Спина", callback_data="Back woman")
            ],
            [
                InlineKeyboardButton(text="Грудь", callback_data="Breast woman")
            ],
            [
                InlineKeyboardButton(text="Руки", callback_data="Hands woman")
            ],
            [
                InlineKeyboardButton(text="Кардио", callback_data="Cardio woman")
            ],
            [
                InlineKeyboardButton(text="Кор", callback_data="Cor woman")
            ],
            [
                InlineKeyboardButton(text="Пресс", callback_data="Press woman")
            ],
            [
                InlineKeyboardButton(text="Фулл-боди", callback_data="Full-body woman")
            ],
            [
                InlineKeyboardButton(text="Заминка", callback_data="Hitch woman")
            ],
            [
                InlineKeyboardButton(text="📝 Указать информацию о себе", callback_data="set_info")
            ]
        ]
    )

    await callback.message.edit_text("Вы выбрали 💪Тренировки для женщин", reply_markup=keyboard)
    await callback.answer()


@trainings.callback_query (F.data == "trainings of man")
async def handle_trainingsofwoman(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Разминка", callback_data="Warm-up man")
            ],
            [
                InlineKeyboardButton(text="Бицепс", callback_data="Biceps man")
            ],
            [
                InlineKeyboardButton(text="Спина", callback_data="Back man")
            ],
            [
                InlineKeyboardButton(text="Трапеция", callback_data="Trapeze man")
            ],
            [
                InlineKeyboardButton(text="Задняя дельта", callback_data="Rear delta man")
            ],
            [
                InlineKeyboardButton(text="плечи(дельты)", callback_data="Shoulders man")
            ],
            [
                InlineKeyboardButton(text="Трицепс", callback_data="Triceps man")
            ],
            [
                InlineKeyboardButton(text="Ноги", callback_data="Legs man")
            ],
            [
                InlineKeyboardButton(text="Грудь", callback_data="Breast man")
            ],
            [
                InlineKeyboardButton(text="Фулл-боди", callback_data="Full-body man")
            ],
            [
                InlineKeyboardButton(text="Заминка", callback_data="Hitch man")
            ],
            [
                InlineKeyboardButton(text="📝 Указать информацию о себе", callback_data="set_info")
            ]
        ]
    )

    await callback.message.edit_text("Вы выбрали 💪Тренировки для мужчин", reply_markup=keyboard)
    await callback.answer()

    @trainings.callback_query(F.data == "Warm-up woman")
    async def handle_trainings(callback: types.CallbackQuery):
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="💪 Тренировки для женщин", callback_data="trainings of woman")
                ],
                [
                    InlineKeyboardButton(text="💪 Тренировки для мужчин", callback_data="trainings of man")
                ],
                [
                    InlineKeyboardButton(text="📝 Указать информацию о себе", callback_data="set_info")
                ]
            ]
        )
        await callback.message.edit_text("Выберите для кого тренировки", reply_markup=keyboard)
        await callback.answer()
