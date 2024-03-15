# Note: Buff163 does not release its statistics on rate limits, but upon testing, a total of 3 scrapers at a time works best
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import re
import os
import pickle
import sys



import asyncio

from helpers import readJson, getFloats, getWeaponsFromCollection, findIds, calculateBest, Buff, config, Apicaller


# The notifier function
 

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


def scrape(collection, grade, desiredFloat, statty=False):
    ids = []

    weapons = getWeaponsFromCollection(collection, grade)

    #remove items not working
    remove = []
    for i in remove:
        weapons.remove(i)


    for weapon in weapons:
        ids.append(findIds(weapon, desiredFloat, statty=statty))

        
    with open("currentids.txt", "w") as f:
        for id in ids:
            for i in id:

                f.write(i)
                f.write("\n")

    with open("currentids.txt", "r") as f:
        lines = f.readlines()
        ids = []

        for line in lines:
            ids.append(line)
        buffApiCaller = Buff(
            goods_ids=ids, request_kwargs=config['buff']['requests_kwargs'])

        output, outs_ids = buffApiCaller.get_total_page()

    readJson(output, outs_ids)
    results = calculateBest(desiredFloat)
    print(results)
    skins = getFloats(results['choices'])
    return results, skins


# Note: if you want an example of a function run, uncomment this:



# add readme.md
