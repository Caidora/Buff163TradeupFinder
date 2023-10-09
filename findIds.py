def findIds(toFind, desiredFloat):

    csv_filename = 'buffids.txt'
    ids = []
    conditions = []
    if desiredFloat < 0.10:
        conditions.append("(Factory New)")
        conditions.append("(Minimal Wear)")
    else:
        conditions.append("(Factory New)")
        conditions.append("(Minimal Wear)")
        conditions.append("(Field-Tested)")
    with open(csv_filename, encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            print(line)
            curline = line.strip().split(';')


            print(curline[1])
            if (curline[1][:len(toFind)] == toFind) and (curline[1][len(toFind)+1:] in conditions):
                ids.append(curline[0])

    with open("currentids.txt", "w") as f:
        for id in ids:

            f.write(id)
            f.write("\n")
