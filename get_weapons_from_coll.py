import json

def get_weapons_from_coll(coll, grade):
    with open('collections.json') as f:
       collections = json.load(f)
    return collections[coll][grade]

#get_weapons_from_coll("Prisma Case", "Mil-Spec")