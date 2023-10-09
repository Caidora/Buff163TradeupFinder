csv_filename = '../output.csv'
items = []
with open(csv_filename) as f:
    lines = f.readlines()
    for line in lines:
        curline = line.strip().split(',')
        newline = list((float(curline[1]), float(curline[2]), 0))
        items.append(newline)
print(items)
for i in range(len(items)):
    items[i][2] = (items[i][1] * items[i][0])


items.sort(key=lambda x: x[2])
for item in items:
    print(item)


def getAverageFloat(comb):
    sums = 0
    for i in comb:
        sums = sums + i[1]
    return (num/10)


def price(comb):
    price = 0
    for i in comb:
        price = price + i[0]
    return (price)


comb = []
for item in items:
    if (len(comb) < 10):
        comb.append(item)
        continue
    currentAverageFloat = getAverage(comb)
