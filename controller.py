from scraper import *
from removeChoices import removeChoices

def main_controller(collection, grade, remove, statty = False):
    weapon_grades = ['Consumer', 'Industrial', 'Mil-Spec', 'Restricted', 'Classified', 'Covert']


    going_for = get_weapons_from_coll(collection, weapon_grades[weapon_grades.index(grade) + 1])
    desired = 100

    for j in remove:
        going_for.remove(j)

    for i in going_for:
        temp = calculate_float(i, 0.07)
        if temp < desired:
            desired = temp
    print(desired)
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



collection = "Operation Breakout Weapon Case"
grade = "Restricted"
remove = ["Five-SeveN | Fowl Play"]
statty = True

#main_controller(collection, grade, remove, statty=statty)


new_float = 0.1
adjust_controller(collection, grade, new_float, statty=statty)

#another_output(collection, grade, new_float, statty, last_output=[]) #find the index of results needed for results