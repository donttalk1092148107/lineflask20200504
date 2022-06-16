import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
nparray = np.array([['姓名','年齡','體重','身高'],
                    ['張三',30,75,165],
                    ['李四',45,60,179],
                    ['王五',55,88,172]])


np.savetxt("firstarray.csv", nparray, delimiter=",",fmt='%s')
data = np.genfromtxt("firstarray.csv",dtype=(int), delimiter=",")
labels=data[0,2:]
mylabels=['體重','身高']
people01=data[1,2:]
people02=data[2,2:]
people03=data[3,2:]

print(labels)
x = np.arange(len(labels))
print(x)
width = 0.35
myfont=FontProperties(fname=r'msjh.ttc')
fig, ax = plt.subplots()
rects1 = ax.bar(x - width, people01, width, label='張三')
rects2 = ax.bar(x - width/2, people02, width, label='李四')
rects3 = ax.bar(x + width/2.5, people03, width, label='王五')
ax.set_ylabel('單位',fontproperties=myfont)
ax.set_title("身高體重",fontproperties=myfont)
ax.set_xticks(x)
ax.set_xticklabels(mylabels,fontproperties=myfont)
ax.legend(prop=myfont)


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width()/3, height),
                    xytext=(0, 2), 
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
fig.tight_layout()

plt.show()


