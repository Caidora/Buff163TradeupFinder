import csv


def readJson(jsons):
    f = open('output.csv', 'w', newline='')
    writer = csv.writer(f)
    for json in jsons:
        items = json['items']
        for item in items:
            asset = item['asset_info']
            wear = asset['paintwear']
            price = item['price']
            writer.writerow([price, wear])

    f.close()
