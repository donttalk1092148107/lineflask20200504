import numpy as np
# int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
dt = np.dtype('i4')
print(dt)


arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr01 = np.array([1, 2, 3, 4],dtype='i8')
print(arr01.dtype)