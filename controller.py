from scraper import *

def main_controller_no_statty(collection, grade, remove):
    weapon_grades = ['Consumer', 'Industrial', 'Mil-Spec', 'Restricted', 'Classified', 'Covert']



    going_for = get_weapons_from_coll(collection, weapon_grades[weapon_grades.index(grade) + 1])
    desired = 100


    for j in remove:
        going_for.remove(j)

    for i in going_for:
        temp = calculate_float(i, 0.07)
        if temp < desired:
            desired = temp

    results, links = scrape(collection, grade, desired)
    ev = ev_calc(results['x_sum'], results['y_mean'], collection, grade)


def main_controller_statty(collection, grade, remove):
    weapon_grades = ['Consumer', 'Industrial', 'Mil-Spec', 'Restricted', 'Classified', 'Covert']


    going_for = get_weapons_from_coll(collection, weapon_grades[weapon_grades.index(grade) + 1])
    desired = 100

    for j in remove:
        going_for.remove(j)

    for i in going_for:
        temp = calculate_float(i, 0.07)
        if temp < desired:
            desired = temp

    results, links = scrape(collection, grade, desired)
    ev = ev_calc(results['x_sum'], results['y_mean'], collection, grade)

def adjust_controller(collection, grade, new_float):
    results = calculateBest(new_float)
    print(results)
    getFloats(results['choices'])


    ev_calc(results['x_sum'], results['y_mean'], collection, grade, statty=False)



collection = "Recoil Case"
grade = "Restricted"
remove = ["Sawed-Off | Kiss♥Love"]

main_controller_no_statty(collection, grade, remove)

#main_controller_statty(collection, grade, remove)

#new_float = 0.07
#adjust_controller(collection, grade, new_float)