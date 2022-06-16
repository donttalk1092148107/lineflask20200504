import csv
with open('0503.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        print(row)
   
