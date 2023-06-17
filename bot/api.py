import aiohttp


class Api():

    async def check_tg_id(self, telegram_id):
        url = 'http://localhost:8000/api/bot/'
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{url}{telegram_id}/') as response:
                return response.status

    async def create_user(self, login, password, telegram_id):
        url = 'http://localhost:8000/api/bot/user/'
        data = {
            "username": login,
            "password": password,
            "profile": {
                "telegram_id": telegram_id
            }
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{url}register/', json=data) as response:
                return response.status

    async def create_task(self, telegram_id, title, description):
        url = 'http://localhost:8000/api/task/'
        data = {
            "telegram_id": telegram_id,
            "title": title,
            "description": description
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{url}create_task/', json=data) as response:
                return response.status

    async def get_tasks(self, telegram_id):
        url = f'http://localhost:8000/api/task/{telegram_id}/get_tasks/'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    tasks = await response.json()
                    return tasks
                return None


api = Api()
