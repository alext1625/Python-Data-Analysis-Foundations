# MINI TASK TO CONSOLIDATE LESSON 5

import pandas as pd

# Load datasets

employees = pd.read_csv("datasets/employees.csv")
projects = pd.read_csv("datasets/projects.csv")

# Join tables

df = pd.merge(employees, projects, how="left", on="employee_id")

# Exercises

df = df[df["hours_per_week"] > 5]       # Filter by hours per week > 5

df = df[(df["department"] == "IT") | (df["department"] == "Sales")]     # Filter by employees in either Sales or IT department

df = df.sort_values("hours_per_week", ascending=False)      # Sort by hours per week, in descending order

df["dept_hours_rank"] = (                           # Rank within their department based on hours per week
    df.groupby("department")["hours_per_week"]
    .rank(ascending = False)
)

print(df)       # Ouput result