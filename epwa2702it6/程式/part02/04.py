import csv
with open('0503.csv', newline='') as csvfile:
  rows = csv.DictReader(csvfile)
  for row in rows:
    print(row['Age'], row['Score'])
