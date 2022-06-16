import csv
with open('0503.csv', "r") as f:
    reader = csv.reader(f)
    #next(reader,None)
    column1 = [row[1] for row in reader]
print (column1)


