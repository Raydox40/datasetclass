import numpy as np
import pandas as pd


arr = np.array([1, 2, 3, 4, 5, 6])

# print(arr)

arr2 = np.array([[1, 2, 3],[4, 5, 6], [1, 2, 3]])
print(arr2)

# index/slicing
print(arr[0])
print(arr[4])
print(arr[-2])
print(arr[1:])

print(arr2[0, 2])

# mathematical operation
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a * b)
print(np.dot(a, b))
print(np.mean(a))
print(np.mean(b))

# pandas operation
ds = pd.Series([10, 20, 40, 50])

print(ds)

data = {
    "name": ["Adesola", "Tolu", "Ayo"],
    "age": [26, 32, 45],
    "city": ["lagos", "oyo", "Aduja"]
}

df =pd.DataFrame(data)

print(df)