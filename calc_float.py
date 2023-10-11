import json
with open('ranges.json') as f:
   dic = json.load(f)

def calculate_float(weapon, desired): #min(lowest) max(highest) of output skin float
    mini, maxi = float(dic[weapon][0]), float(dic[weapon][1])
    return (desired - mini)/(maxi-mini)

def calculate_float_single(mini, maxi): #min(lowest) max(highest) of output skin float
    fac_new = 0.07
    return (fac_new - mini)/(maxi-mini)

#print(calculate_float(0,0.9))

