
def calculateBest():
    csv_filename = 'output.csv'
    indexes = [299, 320, 324, 325, 326, 330, 332, 335, 342, 510]
    items_bought = []

    with open(csv_filename) as f:
        lines = f.readlines()
        for i in range(len(indexes)):
            curline = lines[indexes[i]].strip().split(',')
            items_bought.append(curline)
    print(items_bought)
    sum_of_cost = 0.0
    sum_of_float = 0.0
    for item in items_bought:
        sum_of_cost = sum_of_cost + float(item[1])
        sum_of_float = sum_of_float + float(item[2])
    print(sum_of_cost)
    print(sum_of_float/10)


# calculateBest()
