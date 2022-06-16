# Imports 
import numpy as np
nparray = np.array([[1, 2, 4],[1, 3, 9],[1, 4, 16]])
np.savetxt("firstarray.csv", nparray, delimiter=',')
firstarray = np.genfromtxt("firstarray.csv", delimiter=",")
print(firstarray)


