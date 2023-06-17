
from aiogram.utils import executor
from handlers import start, process_login, process_password, create_task, process_task_title, process_task_description, \
    view_tasks
from config_data.loader_bot import dp

from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware

from states import RegisterForm, CreateTaskForm, UserRegistered

dp.middleware.setup(LifetimeControllerMiddleware())

dp.register_message_handler(start, commands=['start'], state="*")
dp.register_message_handler(process_login, state=RegisterForm.login)
dp.register_message_handler(process_password, state=RegisterForm.password)
dp.register_message_handler(create_task, state="*", commands=['create'])
dp.register_message_handler(process_task_title, state=CreateTaskForm.title)
dp.register_message_handler(process_task_description, state=CreateTaskForm.description)
dp.register_message_handler(view_tasks, state="*", commands=['tasks'])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
