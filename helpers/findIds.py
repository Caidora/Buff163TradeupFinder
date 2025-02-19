def findIds(toFind, desiredFloat, booleanval = 'Normal', statty = False): #boolean to just get fac new etc()

    csv_filename = 'helpers/txt/buffids.txt'
    ids = []
    conditions = []

    #if finding price of fac new/min wear
    if booleanval == 'Normal':
        if desiredFloat < 0.10:
            conditions.append("(Factory New)")
            conditions.append("(Minimal Wear)")
        else:
            conditions.append("(Factory New)")
            conditions.append("(Minimal Wear)")
            conditions.append("(Field-Tested)")
    else:
        conditions.append(booleanval)

    if statty:
        toFind = "StatTrak™ " + toFind

    with open(csv_filename, encoding="utf-8") as f:

        lines = f.readlines()
        for line in lines:
            curline = line.strip().split(';')

            if (curline[1][:len(toFind)] == toFind) and (curline[1][len(toFind)+1:] in conditions):
                ids.append(curline[0])

    return(ids)

