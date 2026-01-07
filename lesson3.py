# LESSON 3: GROUPING, AGGREGATION AND ASKING REAL QUESTIONS

import pandas as pd

# Example Python dictionary
data = {
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [24, 30, 28, 35],
    "salary": [28000, 42000, 35000, 50000],
    "role": ["colleague", "head", "head", "colleague"],
    "department": ["IT", "HR", "IT", "Finance"]
}

df = pd.DataFrame(data)     # Turns data into table (DataFrame)

# Basic groupby example

df.groupby("department")["salary"].mean()   # Calculate average salary per department

# Common aggregations

df.groupby("department")["salary"].mean()           # Average salary per department
df.groupby("department")["salary"].sum()            # Sum of all salaries per department
df.groupby("department")["salary"].count()          # Number of rows per department
df.groupby("department")["salary"].min()            # Lowest salary per department
df.groupby("department")["salary"].max()            # Highest salary per department
df.groupby("department")["salary"].median()         # Median salary per department

# Multiple aggregations simultaneously

df.groupby("department")["salary"].agg(["mean", "min", "max", "count"])     # Give summary table of multiple calculations

# Grouping by multiple columns

df.groupby(["department", "role"])["salary"].mean()     # Create nested groupings 

# Filtering before grouping

filtered = df[df["salary"] > 30000]                 # Filter to only include people with salary > 30000
filtered.groupby("department")["salary"].mean()     # Calculate average salary per department, using filtered records  

# OR one line version:
df[df["salary"] > 30000].groupby("department")["salary"].mean()     # Average salary per department, only including salaries > 30000

# Resetting the index

df.groupby("department")["salary"].mean().reset_index()     # Resets table to default index

# Sorting results

df.groupby("department")["salary"].mean().sort_values(ascending=False)      # Sort results in descending order

