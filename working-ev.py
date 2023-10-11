'''from scraper import *

weapon_grades = ['Consumer', 'Industrial', 'Mil-Spec', 'Restricted', 'Classified', 'Covert']

collection = "Recoil Case"
grade = "Restricted"

going_for = get_weapons_from_coll(collection, weapon_grades[weapon_grades.index(grade) + 1])
desired = 100
remove = ["Sawed-Off | Kiss♥Love"]

for j in remove:
    going_for.remove(j)

for i in going_for:
    temp = calculate_float(i, 0.07)
    if temp < desired:
        desired = temp

results, links = scrape(collection, grade, desired)
ev = ev_calc(results['x_sum'], results['y_mean'], collection, grade)
'''

'''from scraper import *

weapon_grades = ['Consumer', 'Industrial', 'Mil-Spec', 'Restricted', 'Classified', 'Covert']

collection = "CS20 Case"
grade = "Restricted"

going_for = get_weapons_from_coll(collection, weapon_grades[weapon_grades.index(grade) + 1])
desired = 100
remove = ["MP9 | Hydra"]

for j in remove:
    going_for.remove(j)

for i in going_for:
    temp = calculate_float(i, 0.07)
    if temp < desired:
        desired = temp

results, links = scrape(collection, grade, desired)
ev = ev_calc(results['x_sum'], results['y_mean'], collection, grade)'''

'''from scraper import *

weapon_grades = ['Consumer', 'Industrial', 'Mil-Spec', 'Restricted', 'Classified', 'Covert']

collection = "Revolution Case"
grade = "Restricted"

going_for = get_weapons_from_coll(collection, weapon_grades[weapon_grades.index(grade) + 1])
desired = 100
remove = []

for j in remove:
    going_for.remove(j)

for i in going_for:
    temp = calculate_float(i, 0.069)
    if temp < desired:
        desired = temp

results, links = scrape(collection, grade, desired)
ev = ev_calc(results['x_sum'], results['y_mean'], collection, grade)'''



"""from scraper import *

weapon_grades = ['Consumer', 'Industrial', 'Mil-Spec', 'Restricted', 'Classified', 'Covert']

collection = "Prisma 2 Case"
grade = "Restricted"

going_for = get_weapons_from_coll(collection, weapon_grades[weapon_grades.index(grade) + 1])
desired = 100
remove = []

for j in remove:
    going_for.remove(j)

for i in going_for:
    temp = calculate_float(i, 0.069)
    if temp < desired:
        desired = temp

results, links = scrape(collection, grade, desired)
ev = ev_calc(results['x_sum'], results['y_mean'], collection, grade)"""