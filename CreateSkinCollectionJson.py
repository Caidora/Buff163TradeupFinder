import json
ranges = []
names = []


def create_new_collection(outputs,  collection_name):
    raritys = {}
    raritys["Consumer"] = []
    raritys["Industrial"] = []
    raritys["Mil-Spec"] = []
    raritys["Restricted"] = []
    raritys["Classified"] = []
    raritys["Covert"] = []
    outputs[str(collection_name)] = raritys
    return(outputs)



with open("Skins_collections.csv", encoding="utf8") as f:
    lines = f.readlines()
    collections = {}
    for line in lines:
        curline = line.strip().split(',')

        name = curline[0]
        collection = curline[1]
        try:
            cur_collection = collections[collection]
        except KeyError:
            collections = create_new_collection(collections, collection)
            cur_collection = collections[collection]

        rarity = curline[2]
        cur_collection[curline[2]].append(name)

        collections[collection] = cur_collection

    with open("collections.json", "w") as outfile:
        # json_data refers to the above JSON
        json.dump(collections, outfile)





