
import csv
def removeChoices(choices):
    csv_filename = "output.csv"



    with open(csv_filename, "r") as f:
        lines = f.readlines()
        row = 0
        newOutput = []
        for line in lines:
            if(row not in choices):
                newOutput.append(line)

            row = row+1

    f = open('output.csv', 'w', newline='')
    writer = csv.writer(f)
    for line in newOutput:
        curline = line.strip().split(',')
        writer.writerow([curline[0],curline[1]])
    f.close()


