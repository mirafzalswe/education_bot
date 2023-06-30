from aiogram.dispatcher.filters.state import State, StatesGroup


class Register(StatesGroup):
    name = State()
    contact = State()


class Support(StatesGroup):
    teacher = State()


class CourseRegister(StatesGroup):
    days = State()
    times = State()
    phone = State()