# LESSON 1: BASIC DATASET FUNCTIONS

import pandas as pd

# Example Python dictionary
data = {
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [24, 30, 28, 35],
    "salary": [28000, 42000, 35000, 50000],
    "department": ["IT", "HR", "IT", "Finance"]
}

df = pd.DataFrame(data)     # Turns data into table (DataFrame)

# First things to always do with a dataset

df.head()       # Show the first few rows
df.shape        # Return (rows, columns)
df.columns      # List column names

# Selecting data

df["salary"]            # Return salary column as a Series (single column)
df[["name", "salary"]]  # Returns multiple cplumns as a DataFrame

# Filtering rows

df[df["salary"] > 30000]        # Return people earning more than £30,000
df[df["department"] == "IT"]    # Return people in the IT department

# Simple calculations

df["salary"].mean()     # Return avergae salary
df["salary"].max()      # Return lowest salary
df["salary"].min()      # Return highest salary
len(df)                 # Return number of rows

# Grouping data

print(df.groupby("department")["age"].mean())   # Return average salary per department