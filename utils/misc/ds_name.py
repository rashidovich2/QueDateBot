from aiogram import types
from aiogram.utils.markdown import hbold


def get_display_name(user: types.User):
    return f"@{user.username}" if user.username else hbold(user.first_name)
