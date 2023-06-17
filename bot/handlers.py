from aiogram import types
from aiogram.dispatcher import FSMContext
from api import api
from states import RegisterForm, CreateTaskForm


async def start(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    status_code = await api.check_tg_id(telegram_id)
    if status_code == 404:
        await message.answer('Для начала работы с ботом зарегистрируйтесь на сайте. Пожалуйста, придумайте и напишите ваш логин.')
        await state.set_state(RegisterForm.login)
    else:
        await message.answer(f'Добро пожаловать! Вы можете создать задачу с помощью команды /create '
                             f'и просмотреть свои задачи с помощью команды /tasks')


async def process_login(message: types.Message, state: FSMContext):
    user_set_login = message.text
    await state.update_data(user_set_login=user_set_login)
    await message.answer("Теперь придумайте пароль.")
    await RegisterForm.next()


async def process_password(message: types.Message, state: FSMContext):
    user_set_password = message.text
    await state.update_data(user_set_password=user_set_password)
    telegram_id = message.from_user.id
    data = await state.get_data()
    login = data['user_set_login']
    password = data['user_set_password']
    response = await api.create_user(login, password, telegram_id)
    if response == 201:
        await message.answer(
            "Вы успешно зарегистрировались. Теперь с помощью этих логина и пароля можно зайти на сайт http://127.0.0.1:8000/account/. Вы можете создать задачу с помощью команды /create и просмотреть свои задачи с помощью команды /tasks")
    else:
        await message.answer("Ошибка регистрации. Пожалуйста, попробуйте еще раз.")
    await state.finish()


async def create_task(message: types.Message, state: FSMContext):
    await message.answer('Введите название задачи')
    await state.set_state(CreateTaskForm.title)


async def process_task_title(message: types.Message, state: FSMContext):
    user_title = message.text
    await state.update_data(user_title=user_title)
    await message.answer('Введите описание задачи')
    await state.set_state(CreateTaskForm.description)


async def process_task_description(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    user_description = message.text
    await state.update_data(user_description=user_description)
    data = await state.get_data()
    title = data['user_title']
    description = data['user_description']
    await api.create_task(telegram_id, title, description)
    await message.answer('Задача успешно создана')
    await state.finish()


async def view_tasks(message: types.Message):
    telegram_id = message.from_user.id
    tasks = await api.get_tasks(telegram_id)
    if tasks:
        for task in tasks:
            status = "Выполнено" if task['completed'] else "Не выполнено"
            await message.answer(f"Задача: {task['title']}\nОписание: {task['description']}\nСтатус: {status}")
    else:
        await message.answer("У вас пока нет задач.")
