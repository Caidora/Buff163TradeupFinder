from scraper import *
from removeChoices import removeChoices

def main_controller(collection, grade, remove, floatTarget, statty = False):
    weapon_grades = ['Consumer', 'Industrial', 'Mil-Spec', 'Restricted', 'Classified', 'Covert']


    going_for = get_weapons_from_coll(collection, weapon_grades[weapon_grades.index(grade) + 1])
    desired = 100

    for j in remove:
        going_for.remove(j)

    for i in going_for:
        temp = calculate_float(i, floatTarget)

        if temp < desired:
            desired = temp
    print(f"Desired average float of inputs: {desired}")
    results, links = scrape(collection, grade, desired, statty=statty)
    ev = ev_calc(results['x_sum'], results['y_mean'], collection, grade, statty=statty)
    return results

def adjust_controller(collection, grade, new_float, statty = False):
    results = calculateBest(new_float)
    print(results)
    getFloats(results['choices'])

    ev_calc(results['x_sum'], results['y_mean'], collection, grade, statty=statty)

def another_output(collection, grade, new_float, statty=False, last_output=[]):
    removeChoices(last_output)
    results = calculateBest(new_float)
    print(results)

    getFloats(results['choices'])
    ev_calc(results['x_sum'], results['y_mean'], collection, grade, statty=statty)



collection = "Prisma Case" 
grade = "Restricted"
#REMOVE MUST BE FILLED IN WITH OUTCOMES THAT ARE UNABLE TO BE ACHIEVED AT TARGET FLOAT.
remove = ['XM1014 | Incinegator','R8 Revolver | Skull Crusher'] #remove outcomes from float calculation 
statty = False
floatTarget = 0.07 #Factory New
main_controller(collection, grade, remove, floatTarget,statty=statty)

#new_float = 0.202

#adjust_controller(collection, grade, new_float, statty=statty)

#another_output(collection, grade, new_float, statty, last_output=[ 227,  241,  268,  529,  967,  988, 1321, 1338, 2776, 2826]) #find the index of results needed for results