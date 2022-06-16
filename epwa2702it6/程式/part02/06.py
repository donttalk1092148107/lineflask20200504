import csv


with open('0503.csv','r', encoding = "utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    cAge = [row['Age'] for row in reader]
    
    
with open('0503.csv','r', encoding = "utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    cScore = [row['Score'] for row in reader]
print (cAge)
print (cScore)
