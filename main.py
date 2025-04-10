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

# data filtering 
filtering_data = df[df["age"] > 27 ]

print(df)
print(f"Data filtered:{filtering_data}")


# modification
df["age"] =df["age"] + 1

print(df)


# Add custom column
df["Country"] = ['Nigeria', "Nigeria", "Nigeria"]

# Add custom row

data = {
    "Employee": ["Alice", "James", "John", "Samson", "Ademola"],
    "Department": ["HR", "IT", "Finance", "HR", "IT"],
    "Salary": [5000, 3000, 4000, 3200, 44433]
}

df = pd.DataFrame(data)
print(f"Data grouping fram : {df}")

data_grouping = df.groupby("Department")["Salary"].mean()

print(data_grouping)

# data merging
df1 = pd.DataFrame(
    {
        "Employee": ["Alice", "James", "John", "Samson", "musa"],
        "Department": ["HR", "IT", "Finance", "HR", "IT"],

    }
)

df2 = pd.DataFrame({
    "Employee": ["Alice", "James", "John", "Samson", "Ademola"],
    "Salary": [5000, 3000, 4000, 3200, 44433]
})
merged = pd.merge(df1, df2, on="Employee")

print(f"Data Merged: \n {merged}")

# handling missing value
hdf = pd.DataFrame({
    "name": ["Adesola", "Tolu", "Ayo", "Musa"],
    "age": [26, np.nan, 32, np.nan],
    "city": ["lagos", "oyo", "Aduja", np.nan]
})
print(f"Missing Value detected: \n {hdf.isnull()}")

print(f"handling data frame: \n{hdf}")
drop = hdf.dropna()

print(f"New data frame: \n {drop}")

replace_nan = hdf.fillna({"age": hdf["age"].mean(), })