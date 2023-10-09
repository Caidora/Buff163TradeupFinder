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


# obtain list of 10 items wear values and prices for the links found in json file. Returns true if match is found
def obtainItems(id, driver, writer):
    id = str(id)
    idlen = len(id)
    request = "https://buff.163.com/goods/" + str(id[:idlen-1]) + "#page_num="

    curRequest = request + "1"
    print(curRequest)
    driver.get(curRequest)  # driver configs
    cookies = pickle.load(open("../cookies.pkl", "rb"))  # enable cookies
    for cookie in cookies:
        driver.add_cookie(cookie)

    isNamed = True
    try:
        print(driver.find_element(
            By.XPATH, '/html/body/div[7]/div/div[1]/div[2]/div[1]/h1').text, ':\n')
    except NoSuchElementException:
        print('pass')
        isNamed = False
    while True:
        try:
            number = driver.find_element(
                By.XPATH, '/html/body/div[6]/div/div[4]/div[1]/ul/li[1]/a').text
            break
        except NoSuchElementException:
            time.sleep(0.5)
            continue

    x = re.search("\((\d+)\)", number)
    if x == None:
        quantity = 1000
    else:
        amount = x.group()
        quantity = amount.replace('(', '').replace(')', '')
        print(quantity)
    quantity = int(quantity)
    pages = quantity // 10
    pages = pages-1
    lastPageitems = quantity-(pages*10)
    print("pages", pages)
    print("quantity", quantity)
    print("lastpageitems", lastPageitems)

    for j in range(pages):
        getPagesItems(driver, request, j, writer, 10)

    driver.quit


def getPagesItems(driver, request, j, writer, items):
    curRequest = request + str(j+1)
    driver.get(curRequest)
    offset = 0
    for i in range(items):

        while True:
            try:
                wear = driver.find_element(
                    By.XPATH, '/html/body/div[6]/div/div[7]/table/tbody/tr[{}]/td[3]/div/div[1]/div[1]'.format(i+2+offset))
                # consistent html behavior across different item links for CS:GO
                price = driver.find_element(
                    By.XPATH, '/html/body/div[6]/div/div[7]/table/tbody/tr[{}]/td[5]/div[1]/strong'.format(i+2+offset))
            except NoSuchElementException:
                print("could not locate item")
                try:
                    column = driver.find_element(
                        By.XPATH, '/html/body/div[6]/div/div[7]/table/tbody/tr[{}]'.format(i+2+offset))
                    objectclass = column.get_attribute("class")
                    if objectclass[0] == "d":
                        offset = offset+1
                    continue
                except NoSuchElementException:
                    continue

            weartext = float(
                ''.join(c for c in wear.text if c.isdigit() or c == '.'))

            rowString = ""
            itemNumber = ("{}".format((j*10) + i+1))
            price = str(price.text[1:])
            writer.writerow([itemNumber, price, weartext])
            print("found", itemNumber)
            break

