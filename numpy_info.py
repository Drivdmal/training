import numpy as np
import pandas as pd

# make list
numbers = [2,3,4,5,6,4,3,4,5,4,5]
numbers2 = [2,3,3,4,3,3,3,3,2,5,6]
# make array numpy
vector1 = np.array(numbers)
vector2 = np.array(numbers2)
# make DataFrame
data1 = pd.DataFrame(numbers)
data2 = pd.DataFrame(vector1)
print(data1[0].values)
print(data2)
# сколярное произведение
print(np.dot(vector1,vector2))
# то же самое
print(vector1 @ vector2)
# создать вектор из нулей
np.zeros(10)