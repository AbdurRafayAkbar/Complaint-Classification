import pandas as pd

df = pd.read_csv("data/complaints_100.csv")

head=df.head()
tail=df.tail()
desc=df.describe()
info=df.info()
shape=df.shape
missing_values=df.isnull().sum()
duplicate_values=df.duplicated().sum()

# print(head)
# print(tail)
# print(desc)
# print(info)
# print(shape)
# print(missing_values)
# print(duplicate_values)

# MATPLOT

# import matplotlib.pyplot as plt

# category_count=df["Category"].value_counts()

# plt.figure(figsize=(8,5))

# plt.bar(category_count.index,category_count.values)

# plt.title("Complaint Categorizing")

# plt.xlabel("Category")

# plt.ylabel("Number of Complaints")

# plt.show()

