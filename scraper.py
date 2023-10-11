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
from Readjson import readJson
from getFloats import getFloats
from get_weapons_from_coll import get_weapons_from_coll
from calc_ev import ev_calc
import asyncio
# The notifier function


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


def scrape(collection, grade, desiredFloat):
    ids = []

    weapons = get_weapons_from_coll(collection, grade)
    for weapon in weapons:
        ids.append(findIds(weapon, desiredFloat))
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

        output = buffApiCaller.get_total_page()

    readJson(output)
    results = calculateBest(desiredFloat)
    print(results)
    skins = getFloats(results['choices'])
    return results, skins


if len(sys.argv) != 4:
    print('Please enter the correct number of arguments')
    pass
else:
    scrape(int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]))

# Note: if you want an example of a function run, uncomment this:
#weapon_grades = ['Consumer','Industrial','Mil-Spec','Restricted','Classified','Covert']

#scrape("Prisma Case", "Mil-Spec", 0.077)

collection = "Prisma Case"
grade = "Restricted"

results, links = scrape(collection, grade, 0.07)
ev = ev_calc(results[0]['x_sum'], results[0]['y_mean'], collection, grade)


# add readme.md
