import json

def getWeaponsFromCollection(coll, grade):
    with open('helpers/json/collections.json') as f:
       collections = json.load(f)
       
    return collections[coll][grade]

#get_weapons_from_coll("Prisma Case", "Mil-Spec")