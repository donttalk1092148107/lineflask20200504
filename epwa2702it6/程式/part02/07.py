import csv
import numpy as np
import matplotlib.pyplot as plt

with open('0503.csv','r', encoding = "utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    cAge = [int(row['Age']) for row in reader]
    
with open('0503.csv','r', encoding = "utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    cScore = [int(row['Score']) for row in reader]

with open('0503.csv','r', encoding = "utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    cName = [row['Name'] for row in reader]

print (cAge)
print (cScore)

FcAge=tuple(cAge)
FcScore=tuple(cScore)
print(FcAge)
print(FcScore)

N = 5
#menMeans = (12,13,14,15,16)
#womenMeans = (80,70,75,60,66)
menMeans =FcAge
womenMeans=FcScore
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)
width = 0.35

p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans, yerr=womenStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, cName)
plt.yticks(np.arange(0, 80, 10))
plt.legend((p1[0], p2[0]), ('Age', 'Score'))

plt.show()
