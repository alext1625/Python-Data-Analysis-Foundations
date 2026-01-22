# LESSON 5: FILTERING, SORTING AND RANKING DATA

import pandas as pd

# Load datasets

employees = pd.read_csv("datasets/employees.csv")
projects = pd.read_csv("datasets/projects.csv")

# Join tables

df = pd.merge(employees, projects, how="left", on="employee_id")

# Filter row

df[df["hours_per_week"] >= 10]      

# Filter with multiple conditions 

df[(df["department"] == "IT") & (df["hours_per_week"] >= 10)]       # With AND condition
df[(df["department"] == "IT") | (df["department"] == "Sales")]      # With OR condition

# Filtering using .isin()

df[df["department"].isin(["IT", "Sales"])]

# Sort by hours per week

df.sort_values("hours_per_week")
df.sort_values("hours_per_week", ascending=False)   # Descending order

# Sort by multiple columns

df.sort_values(           
    by=["department", "hours_per_week"],        # Sort first by department in alphabetical order
    ascending=[True, False]                     # then by hours per week in descending order
)

# Rank employees by hours worked

df["hours_rank"] = df["hours_per_week"].rank(ascending=True)

# Rank within each department 

df["dept_hours_rank"] = (
    df.groupby("department")["hours_per_week"]
      .rank(ascending=True)
)

