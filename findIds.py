toFind = "Glock-18 | Oxide Blaze"

csv_filename = 'buffids.txt'
ids = []
with open(csv_filename) as f:
    lines = f.readlines()
    for line in lines:
        print(line)
        curline = line.strip().split(';')
        print(curline[1])
        if (curline[1][:len(toFind)] == toFind):
            ids.append(curline[0])

with open("currentids.txt", "w") as f:
    for id in ids:

        f.write(id)
        f.write("\n")
