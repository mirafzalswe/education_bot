from aiogram.dispatcher.filters.state import State, StatesGroup


class TeachersState(StatesGroup):
    text = State()
