from aiogram.dispatcher.filters.state import State, StatesGroup


class AddCourseState(StatesGroup):
    text = State()
