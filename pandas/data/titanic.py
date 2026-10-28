# https://pandas.pydata.org/docs/getting_started/index.html

import pandas as pd
import csv

"# Reading the Titanic dataset from a CSV file into a pandas DataFrame"
titanic = pd.read_csv("pandas/data/titanic.csv")


"# creating an Excel file from the titanic DataFrame"
# titanic.to_excel("pandas/data/titanic.xlsx", sheet_name="passengers", index=False)

"# Reading the Excel file back into a DataFrame using the openpyxl engine"
# titanic = pd.read_excel(
#     "pandas/data/titanic.xlsx", sheet_name="passengers", engine="openpyxl"
# )

"# Display the DataFrame"
# print(titanic)

"# I want to see the first 8 rows of a pandas DataFrame."
# print(titanic.head(8))

"# Get the last 5 rows of a DataFrame."
# print(titanic.tail(5))


"# Display the shape and data types of the titanic DataFrame."
# print(titanic.shape)
# print(titanic.dtypes)

"# Display information about the DataFrame"
# print(titanic.info())

"# I’m interested in the age of the Titanic passengers."
# ages = titanic["Age"]
# print(ages.head())

"# checking type and shape"
# print(type(titanic["Age"]))
# print(titanic["Age"].shape)

"# accessing bot age and sex"
# age_sex = titanic[["Age", "Sex"]]
# print(age_sex.head())


# print(type(titanic[["Age", "Sex"]]))
# print(titanic[["Age", "Sex"]].shape)

"# I’m interested in the passengers older than 35 years."
# above_35 = titanic[titanic["Age"] > 35]
# print(above_35.head())

# above_35.to_csv("pandas/data/new.csv", index=False)
# new_df = pd.read_csv("pandas/data/new.csv")
# print(new_df.head())


"# 1. Writing to new.csv using csv.writer"
# with open("pandas/data/new.csv", mode="w", newline="", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     # Write the column headers
#     writer.writerow(above_35.columns)
#     # Write all data rows
#     writer.writerows(above_35.values)

"# 2. Reading from new.csv using csv.reader"
# with open("pandas/data/new.csv", mode="r", newline="", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)


"# I’m interested in the Titanic passengers from cabin class 2 and 3."
# class_2_and_3 = titanic[titanic["Pclass"].isin([2, 3])]
# print(class_2_and_3.head())

"# The above is equivalent to filtering by rows for which the class is either 2 or 3 and combining the two statements with an | (or) operator:"
# class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
# print(class_23.head())

"# I want to work with passenger data for which the age is known."
# age_no_na = titanic[titanic["Age"].notna()]
# print(age_no_na.head())
# print(age_no_na.shape)

"# How do I select specific rows and columns from a DataFrame?"
"# I’m interested in the names of the passengers older than 35 years."
# adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
# print(adult_names.head())

"# I’m interested in rows 10 till 25 and columns 3 to 5."
# print(titanic.iloc[9:25, 2:5])

"# When selecting specific rows and/or columns with loc or iloc, new values can be assigned to the selected data. For example, to assign the name anonymous to the first 3 elements of the fourth column:"
# titanic.iloc[0:3, 3] = "anonymous"
# print(titanic.iloc[:5, 3])


"""
REMEMBER
1.When selecting subsets of data, square brackets [] are used.

2.Inside these square brackets, you can use a single column/row label, a list of column/row labels, a slice of labels, a conditional expression or a colon.

3.Use loc for label-based selection (using row/column names).

4.Use iloc for position-based selection (using table positions).

5.You can assign new values to a selection based on loc/iloc.

"""
