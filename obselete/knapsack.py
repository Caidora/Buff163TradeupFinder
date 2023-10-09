import copy
def getAverageFloat(comb):
    sums = 0
    for i in comb:
        sums = sums + i[1]
    return (sums/10)


def getPrice(comb):
    price = 0
    for i in comb:
        price = price + i[0]
    return (price)


def calculateBest(target_float):
    csv_filename = '../output.csv'
    items = []
    with open(csv_filename, encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            curline = line.strip().split(',')
            newline = list((float(curline[1]), float(curline[2]), 0))
            items.append(newline)

    for i in range(len(items)):
        items[i][2] = (items[i][1] / items[i][0])

    target_val = target_float

    # Task: Minimize the sum of 10 elements(x) while keeping sum of corresponding y values less
    # less than target_val

    # Step 1: Sort the list based on x values
    items.sort(key=lambda x: x[2])

    print(items)
    # Step 2: Take a window of size 10 and find the sum of x values and corresponding y values
    Knapsack = []
    for item in items:
        if len(Knapsack)<10:
            Knapsack.append(item)
            continue
        price = getPrice(Knapsack)
        possibleNewSack = []
        possibleNewPrice = 0
        for i in range(len(Knapsack)):
            newSack = copy.deepcopy(Knapsack)
            print(newSack)
            newSack[i] = item
            newAverageFloat = getAverageFloat(newSack)
            newPrice = getPrice(newSack)
            if(getAverageFloat(Knapsack)>target_float):
                if((possibleNewSack is None) or newPrice<possibleNewPrice):
                    possibleNewSack = newSack
                    possibleNewPrice = newPrice
            if((newAverageFloat<target_float) and (newPrice<price)):
                if((possibleNewSack is None) or newPrice<possibleNewPrice):
                    possibleNewSack = newSack
                    possibleNewPrice = newPrice
        Knapsack = possibleNewSack


    print("Window: ", Knapsack)
    print("price: ", getPrice(Knapsack))
    print("avg float: ", getAverageFloat(Knapsack))



calculateBest(0.1166)
