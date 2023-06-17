from aiogram.dispatcher.filters.state import StatesGroup, State

class RegisterForm(StatesGroup):
    login = State()
    password = State()


class CreateTaskForm(StatesGroup):
    title = State()
    description = State()


class UserRegistered(StatesGroup):
    user_registered = State()