# LESSON 2: LOADING, CLEANING AND EXPLORING DATA

import pandas as pd

# Loading dataset (CSV, using ; as seperator)
df = pd.read_csv("datasets/data.csv", sep=";")

# First things to always do with CSV

df.info()                           # Return column names, data types and null (missing) values
df.describe()                       # Return mean, min/max, standard deviation and quartiles for all numeric columns
df["Identifier"].describe()         # Return only for Identifier column
df[["Identifier", "_"]].describe()  # Return for multiple selected columns

# Handling missing data

df.isnull().sum()       # Return number of missing values
df.dropna()             # Drop rows with missing data

# Fill missing values, in this case fill all missing Identifier values with the mean of all other Identifier values
df["Identifier"] = df["Identifier"].fillna(df["Identifier"].mean())

# Sorting and ranking data

df.sort_values(by="Identifier", ascending=False)            # Sort by Identifier column in descending order
df.sort_values(by="Identifier", ascending=False).head(3)    # Return the top 3 entries of these

# Creating new columns

df["Double_identifier"] = df["Identifier"] * 2      # Create new column Double_identifier from double the Identifier value
df["High_identifier"] = df["Identifier"] > 5000     # Create new column High_identifier labeling those with high identifiers, having an Identifier value > 5000

# Combining filters and grouping

df[df["Identifier"] > 5000].groupby("Department")["Identifier"].mean()  # Return average of Indentifier values per department for people with identifier values > 5000

print(df.head())
