import json, csv


def readJson():
    with open("api.json", encoding="utf8") as f:
        data = json.load(f)

    data = data['data']
    items = data['items']

    f = open('output.csv', 'w', newline='')
    writer = csv.writer(f)

    for item in items:
        asset = item['asset_info']
        wear = asset['paintwear']
        price = item['price']
        writer.writerow([price, wear])

    f.close()
