import json
ranges = []
names = []
with open("txt/buffskinrange.txt", encoding="utf8") as f:
    lines = f.readlines()
    for line in lines:
        curline = line.strip().split(',')

        name = curline[0]
        floatRange = [curline[1],curline[2]]
        if "�" in name:
            ind = name.index("�")
            name = name[:ind] + "ö" + name[ind+1:]
        ranges.append(floatRange)
        names.append(name)


with open("txt/buffids.txt", encoding="utf8") as f:
    lines = f.readlines()
    dic = {}
    for line in lines:

        curline = line.strip().split(';')
        jname = curline[1].split('(')[0].strip()

        if jname in names:
            if jname not in dic:
                dic[jname] = ranges[names.index(jname)]

            #print(names[names.index(curline[1].split('(')[0].strip())],curline[0])

with open("json/ranges.json", "w") as outfile:
    # json_data refers to the above JSON
    json.dump(dic, outfile)

print(dic)
for i in names:
    if i not in dic and "Knife |" not in i and "Daggers |" not in i and "Bayonet |" not in i and "Karambit |" not in i:
        print(i)

