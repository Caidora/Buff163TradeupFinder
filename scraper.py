# Note: Buff163 does not release its statistics on rate limits, but upon testing, a total of 3 scrapers at a time works best
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import re
import os
import pickle
import sys
from findIds import findIds
from calculateBest import calculateBest
from Apicaller.retrieveJson import Buff
from Apicaller import config
import asyncio
# The notifier function


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


def scrape(weapon, desiredFloat):
    findIds(weapon)


    with open("currentids.txt", "r") as f:
        lines = f.readlines()
        ids = []

        for line in lines:
            ids.append(line)
        buffApiCaller = Buff(goods_ids=ids, request_kwargs=config['buff']['requests_kwargs'])
        output = buffApiCaller.get_total_page()

    Readjson(output)
    print(calculateBest(desiredFloat))


if len(sys.argv) != 4:
    print('Please enter the correct number of arguments')
    pass
else:
    scrape(int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]))

# Note: if you want an example of a function run, uncomment this:
scrape("AWP | Wildfire", 0.086)

# add readme.md
