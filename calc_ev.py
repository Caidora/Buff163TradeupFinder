from findIds import findIds
from Apicaller.retrieveJson import Buff
from Apicaller import config
from get_weapons_from_coll import get_weapons_from_coll

import json

with open('ranges.json', encoding='utf-8') as f:
   dic = json.load(f)

weapon_grades = ['Consumer','Industrial','Mil-Spec','Restricted','Classified','Covert']
def float_out(rangearr,avg):
    mini = float(rangearr[0])
    maxi = float(rangearr[1])
    return (maxi-mini)*avg + mini


def ev_calc(cost, avgfloat, inputcoll, inputgrade,statty=False):
    outputs = get_weapons_from_coll(inputcoll,weapon_grades[weapon_grades.index(inputgrade)+1])
    wear = []
    check_over = []
    over_floats = []
    ids = []

    for out in outputs:
        floatOf = float_out(dic[out], avgfloat)
        if floatOf < 0.05 or (floatOf > 0.07 and floatOf < 0.1):
            check_over.append(out)
            over_floats.append(floatOf)
        if floatOf < 0.07:
            wear.append(out + " (Factory New)")
            ids.append(findIds(out,0,"(Factory New)",statty=statty))
        elif floatOf < 0.15:
            wear.append(out + " (Minimal Wear)")
            ids.append(findIds(out, 0, "(Minimal Wear)",statty=statty))
        else:
            wear.append(out + " (Field-Tested)")
            ids.append(findIds(out, 0, "(Field-Tested)",statty=statty))

    with open('output_price.txt', 'r') as f:
        outputs_check = f.readline().strip()
        out_price_check = f.readline().strip()
        stat_check = f.readline()

    if outputs_check != str(outputs) or stat_check != "Stat =" + str(statty):
        buffApiCaller = Buff(
            goods_ids=ids, request_kwargs=config['buff']['requests_kwargs'])
        pricejsons = buffApiCaller.get_item_prices()

        out_price = []

        for json in pricejsons:
            items = json['items']
            out_price.append(float(items[0]['price']))

        with open('output_price.txt', 'w', encoding='utf-8') as f:
            f.write(str(outputs))
            f.write("\n")
            f.write(str(out_price))
            f.write("\n")
            f.write("Stat =" + str(statty))
    else:
        out_price = eval(out_price_check)



    profit = (sum(out_price)/len(out_price))-cost
    ev = (profit+cost)/cost*100
    print(out_price)
    print("Check overpay(<0.05): " + repr(check_over))
    print(wear)
    print("Total cost: "+ "$"+str(cost))
    print("EV: "+str(ev)+"%")
    print("Profit per Trade-Up: $" + str(profit))
    for i in outputs:
        print("Profit on {}: ${}".format(i, out_price[outputs.index(i)]-cost))

    for over in check_over:
        over_ind = outputs.index(over)
        new_price = float(input("\nEnter overpay price for {} ({}): ".format(over,over_floats[check_over.index(over)])))
        out_price[over_ind] = new_price

    if len(check_over)>0:
        profit = (sum(out_price) / len(out_price)) - cost
        ev = (profit + cost) / cost * 100

        print("\nNew EV:")
        print(wear)
        print("Total cost: " + "$" + str(cost))
        print("EV: " + str(ev) + "%")
        print("Profit per Trade-Up: " + str(profit))
        for i in outputs:
            print("Profit on {}: ${}".format(i, out_price[outputs.index(i)]-cost))
    return ev

#ev_calc(results[0]['x_sum'], results[0]['y_mean'], collection, grade)




