# import os
# import sys
#
# import django
# from asgiref.sync import sync_to_async
#
# sys.path.append(os.path.abspath('../../'))
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_list.todo_list.settings')
# django.setup()
#
# from account.models import Profile, Task
# from django.contrib.auth.models import User
#
#
# async def get_user(telegram_id):
#     '''Потдверждение регистрации юзера'''
#     queryset = await sync_to_async(Profile.objects.filter, thread_sensitive=True)(telegram_id=telegram_id)
#     user = await sync_to_async(queryset.first, thread_sensitive=True)()
#     return user
#
#
# async def register_user(login, password, telegram_id):
#     '''Регистрация нового пользователя'''
#     new_user = await sync_to_async(User.objects.create_user, thread_sensitive=True)(username=login, password=password)
#     new_profile = await sync_to_async(Profile.objects.create, thread_sensitive=True)(user=new_user, telegram_id=telegram_id)
#     return new_profile
#
#
# async def set_task(title, description, telegram_id):
#     '''Создание новой задачи'''
#     user = await sync_to_async(User.objects.get, thread_sensitive=True)(profile__telegram_id=telegram_id)
#     await sync_to_async(Task.objects.create, thread_sensitive=True)(user=user, title=title, description=description)
#
#
# async def get_tasks(telegram_id):
#     '''Извлечение задач пользователя'''
#     user = await sync_to_async(User.objects.get, thread_sensitive=True)(profile__telegram_id=telegram_id)
#     queryset = await sync_to_async(Task.objects.filter, thread_sensitive=True)(user=user)
#     tasks = await sync_to_async(list, thread_sensitive=True)(queryset)
#     return tasks
