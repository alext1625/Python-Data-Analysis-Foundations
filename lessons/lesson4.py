# LESSON 4: MERGING AND JOINING DATA FRAMES

import pandas as pd

# Load datasets

employees = pd.read_csv("datasets/employees.csv")
salaries = pd.read_csv("datasets/salaries.csv")
projects = pd.read_csv("datasets/projects.csv")

# Join examples

merged_inner = pd.merge(employees, salaries, how = "inner", on = "employee_id")     # Inner join
merged_left = pd.merge(employees, salaries, how = "left", on = "employee_id")       # Left join
merged_right = pd.merge(employees, salaries, how = "right", on = "employee_id")     # Right join
merged_outer = pd.merge(employees, salaries, how = "outer", on = "employee_id")     # Outer join

# Group by department and calculate average salary per department

averageSalaryPerDepartment = merged_left.groupby("department")["salary"].mean()

# Add a column to new left merged table for high earners

merged_left["high_earner"] = merged_left["salary"] > 55000

# Merge employees and projects for various purposes

employeesWithProjects = pd.merge(employees, projects, how = "inner", on = "employee_id")        # All employees assigned to a project
allEmployees = pd.merge(employees, projects, how = "left", on = "employee_id")                  # All employees, both with or without projects
allEmployeesAndProjects = pd.merge(employees, projects, how = "outer", on = "employee_id")      # All employees and projects

# Calculate average hours per department

averageHoursPerDepartment = employeesWithProjects.groupby("department")["hours_per_week"].mean()

# Add column for projects that are considered full time based on hours per week

employeesWithProjects["full_time_project"] = employeesWithProjects["hours_per_week"] >= 20

# Count how many employees per department are working full time on projects

fullTimeCount = employeesWithProjects[employeesWithProjects["full_time_project"]].groupby("department")["employee_id"].count()  
# Groups employees that are working full time on projects by department, and counts number of employees per department

fullTimeCountAlt = employeesWithProjects.groupby("department")["full_time_project"].sum()   # Alternative shorter method

# Calculate the percentsage of full-time project employees per department

employeesPerDepartment = employees.groupby("department")["employee_id"].count()                 # Total employees per department
fullTimePerDepartment = employeesWithProjects.groupby("department")["full_time_project"].sum()  # Total full-time project employees per department
percentage = ((fullTimePerDepartment / employeesPerDepartment) * 100).fillna(0)                 # Calculate percentage 

# Create a summary table

summary = pd.DataFrame({
    "total_employees": employeesPerDepartment,
    "full_time_project_employees": fullTimePerDepartment,
    "percent_full_time_project": percentage
})

summary = summary.fillna(0)     # Replaces NaN valuees with 0

print(summary)