import pandas as pd

df = pd.read_csv("data/complaints_100.csv")

head=df.head()
tail=df.tail()
desc=df.describe()
info=df.info()
shape=df.shape
missing_values=df.isnull().sum()
duplicate_values=df.duplicated().sum()

print(head)
print(tail)
print(desc)
print(info)
print(shape)
print(missing_values)
print(duplicate_values)