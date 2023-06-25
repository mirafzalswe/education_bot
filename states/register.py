from aiogram.dispatcher.filters.state import State, StatesGroup


class Profilestates(StatesGroup):
    name = State()
    age = State()
    contakt = State()
