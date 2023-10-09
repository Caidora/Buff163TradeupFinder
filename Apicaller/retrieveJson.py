import asyncio
import re
import time

import httpx, random

from datetime import datetime

from Apicaller.exceptions import BuffError

def epochTimestamp():
    return int(round(datetime.now().timestamp()*1000))

class Buff:
    base_url = 'https://buff.163.com'
    web_sell_order = '/api/market/goods/sell_order'


    csrf_pattern = re.compile(r'name="csrf_token"\s*content="(.+?)"')

    def __init__(self, goods_ids, game='csgo', game_appid=730, request_interval=10, request_kwargs=None):
        if request_kwargs is None:
            request_kwargs = {}

        self.request_interval = request_interval
        self.request_locks = {}  # {url: [asyncio.Lock, last_request_time]}
        self.headers = request_kwargs[0]
        self.cookies = request_kwargs[1]
        self.request_ids = goods_ids
        self.game = game
        self.game_appid = game_appid
        self.opener = httpx.AsyncClient(base_url=self.base_url, headers=self.headers, cookies=self.cookies)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.opener.aclose()

    async def request(self, *args, **kwargs) -> dict:

        response = await self.opener.request(*args, **kwargs)
        if response.json()['code'] != 'OK':
            print("oh shit something went wrong")
            raise BuffError(response.json())

        return response.json()['data']

    async def get_total_page(self):
        outputs = []
        for id in self.request_ids:

            response = await self.request('get', self.web_sell_order, params={
                'game': self.game,
                'goods_id': id,
                'page_num': 1,
                'page_size': 2000,
                "_": {epochTimestamp()}
            })
            outputs.append(response)
            time.sleep(random.randint(5,15))


        return outputs
