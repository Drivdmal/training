import numpy as np
import pandas as pd


numbers = [2,3]

vector1 = np.array(numbers)

data = pd.DataFrame([1, 2, 3, 4])

print(vector1)
print(numbers)
print(data[0].values)
print(list(vector1))