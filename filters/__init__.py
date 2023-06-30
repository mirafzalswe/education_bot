from aiogram import Dispatcher

from loader import dp
from .customs import IsAdmin, IsTeacher


if __name__ == "filters":
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsTeacher)

