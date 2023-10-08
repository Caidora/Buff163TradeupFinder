

def calculateBest(target_float):
    csv_filename = 'output.csv'
    items = []
    with open(csv_filename) as f:
        lines = f.readlines()
        for line in lines:
            curline = line.strip().split(',')
            newline = list((float(curline[1]), float(curline[2]), 0))
            items.append(newline)
    print(items)

    target_val = target_float

    # Task: Minimize the sum of 10 elements(x) while keeping sum of corresponding y values less
    # less than target_val

    # Step 1: Sort the list based on x values
    items.sort(key=lambda x: x[0])

    # Step 2: Take a window of size 10 and find the sum of x values and corresponding y values
    window_x_sum = 0
    window_y_sum = 0

    for i in range(10):
        window_x_sum += items[i][0]
        window_y_sum += items[i][1]

    left_pointer = 0
    right_pointer = 10

    # Before we start moving the window, we need to check whether the window_y satisfies the condition
    # If it does, we have already found the solution
    if (window_y_sum / 10) < target_val:
        print("Solution found")
        print("Window: ", items[left_pointer:right_pointer])
        print("Window x sum: ", window_x_sum)
        print("Window y avg: ", window_y_sum/10)
    else:
        while right_pointer < len(lines):
            window_x_sum -= items[left_pointer][0]
            window_y_sum -= items[left_pointer][1]
            left_pointer += 1
            window_x_sum += items[right_pointer][0]
            window_y_sum += items[right_pointer][1]
            right_pointer += 1
            if (window_y_sum / 10) < target_val:
                print("Solution found")
                print("Window: ", items[left_pointer:right_pointer])
                print("price: ", window_x_sum)
                print("avg float: ", window_y_sum/10)
                break


calculateBest(0.0905)
