
def getFloats(indexes):
    csv_filename = 'output.csv'
    indexes = indexes
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
        sum_of_cost = sum_of_cost + float(item[0])
        sum_of_float = sum_of_float + float(item[1])
    print(sum_of_cost)
    print(sum_of_float/10)


# calculateBest()
# getFloats([86, 687, 699, 710, 814, 893, 922, 923, 979, 987])
