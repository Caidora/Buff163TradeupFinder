import csv


def getNames():

    with open("currentids.txt") as f:
        ids = f.readlines()
    names = []
    with open("txt/buffids.txt") as f:
        lines = f.readlines()
        for line in lines:
            curline = line.strip().split(';')
            if curline[0] == ids[0]:
                names.append(curline[1])


def readJson(jsons, ids):
    f = open('output.csv', 'w', newline='')
    writer = csv.writer(f)


    for json in jsons:
        items = json['items']
        item_name = json['goods_infos'][ids[0].strip()]['name']
        ids.pop(0)
        for item in items:
            asset = item['asset_info']
            wear = asset['paintwear']
            price = item['price']

            goodsid = asset['goods_id']
            appid = asset['appid']
            classid = asset['classid']
            instanceid = asset['instanceid']
            assetid = asset['assetid']
            sell_id = item['id']
            link_str = "https://buff.163.com/goods/{}?appid={}&classid={}&instanceid={}&assetid={}&contextid=2&sell_order_id={}".format(goodsid,appid,classid,instanceid,assetid,sell_id)
            writer.writerow([price, wear, item_name, link_str])

    f.close()
