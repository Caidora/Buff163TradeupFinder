

import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds




def calculateBest(target_float):
    csv_filename = 'output.csv'
    items = []
    x = []
    y = []
    with open(csv_filename, encoding="windows-1252") as f: #windows-1252 TM
        lines = f.readlines()
        for line in lines:
            curline = line.strip().split(',')
            x.append(float(curline[0]))
            y.append(float(curline[1]))


    target_mean = target_float
    num_choices = 10
    x, y = np.array(x), np.array(y)
    A = np.vstack([np.ones_like(x), y])
    ub = [num_choices, num_choices * target_mean]
    lb = [num_choices, -np.inf]
    #print("num choices".format(num_choices))
    res = milp(x,
               constraints=LinearConstraint(A, ub=ub, lb=lb),
               integrality=np.ones_like(x),
               bounds=Bounds(lb=0, ub=1)
               )
    if res.success:
        choices = np.nonzero(res.x)[0]
        return {"choices": choices,
                "x_sum": res.fun,
                "y_mean": y[choices].mean()}



