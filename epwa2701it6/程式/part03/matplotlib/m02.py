import numpy as np 
from matplotlib import pyplot as plt 
import matplotlib
 
zhfont1 = matplotlib.font_manager.FontProperties(fname="simhei.ttf") 
 
x = np.arange(1,11) 
y =  2  * x +  5 
plt.title("中文測試", fontproperties=zhfont1) 
 

plt.xlabel("x軸", fontproperties=zhfont1)
plt.ylabel("y軸", fontproperties=zhfont1)
plt.plot(x,y) 
plt.show()