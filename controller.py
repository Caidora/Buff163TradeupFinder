from scraper import *
from helpers import removeChoices, calc_ev, calculate_float

def main_controller(collection, grade, remove, floatTarget, statty = False):
    weapon_grades = ['Consumer', 'Industrial', 'Mil-Spec', 'Restricted', 'Classified', 'Covert']


    going_for = getWeaponsFromCollection(collection, weapon_grades[weapon_grades.index(grade) + 1])
    desired = 100

    for j in remove:
        going_for.remove(j)

    for i in going_for:
        temp = calculate_float(i, floatTarget)

        if temp < desired:
            desired = temp
    print(f"Desired average float of inputs: {desired}")
    results, links = scrape(collection, grade, desired, statty=statty)
    ev = calc_ev(results['x_sum'], results['y_mean'], collection, grade, statty=statty)
    return results

def adjust_controller(collection, grade, new_float, statty = False):
    results = calculateBest(new_float)
    print(results)
    getFloats(results['choices'])

    calc_ev(results['x_sum'], results['y_mean'], collection, grade, statty=statty)

def another_output(collection, grade, new_float, statty=False, last_output=[]):
    removeChoices(last_output)
    results = calculateBest(new_float)
    print(results)

    getFloats(results['choices'])
    calc_ev(results['x_sum'], results['y_mean'], collection, grade, statty=statty)

