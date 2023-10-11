import asyncio
import re
import time

import httpx
import random

from datetime import datetime

from Apicaller.exceptions import BuffError


def epochTimestamp():
    return int(round(datetime.now().timestamp()*1000))


class Buff:
    base_url = 'https://buff.163.com'
    web_sell_order = '/api/market/goods/sell_order'

    def __init__(self, goods_ids, game='csgo', game_appid=730, request_interval=10, request_kwargs=None):

        if request_kwargs is None:
            request_kwargs = {}
        self.request_interval = request_interval
        self.request_locks = {}  # {url: [asyncio.Lock, last_request_time]}
        self.headers = request_kwargs['headers']
        self.cookies = request_kwargs['Cookie']
        self.request_ids = goods_ids
        self.game = game
        self.game_appid = game_appid
        self.client = httpx.Client(
            base_url=self.base_url, headers=self.headers, cookies=self.cookies)

    def request(self, params) -> dict:

        response = self.client.get(
            self.web_sell_order, params=params, timeout=10)

        if response.json()['code'] != 'OK':
            print("oh shit something went wrong")
            raise BuffError(response.json())
        else:
            print("GOT REQUEST BACK")
        return response.json()['data']

    def get_total_page(self):
        outputs = []
        for id in self.request_ids:
            print("making request for {}".format(id))
            response = self.request(params={
                'game': self.game,
                'goods_id': id,
                'page_num': 1,
                'page_size': 500,
                "_": {epochTimestamp()}
            })
            outputs.append(response)
            print("appended request going to sleep.zzz")
            time.sleep(random.randint(5, 15))

            item_count = response['total_count']
            more_pages = item_count // 500 - 1
            for i in range(more_pages):
                print("making request for {}, page: {}".format(id,i+2))
                response = self.request(params={
                    'game': self.game,
                    'goods_id': id,
                    'page_num': i+2,
                    'page_size': 500,
                    "_": {epochTimestamp()}
                })
                outputs.append(response)
                print("appended request going to sleep.zzz")
                time.sleep(random.randint(5, 15))


        return outputs

    def get_item_prices(self):
        outputs = []
        for id in self.request_ids:
            print("making request for {}".format(id))
            response = self.request(params={
                'game': self.game,
                'goods_id': id,
                'page_num': 1,
                "_": {epochTimestamp()}
            })
            outputs.append(response)
            print("appended request going to sleep.zzz")
            time.sleep(random.randint(5, 15))

        return outputs
