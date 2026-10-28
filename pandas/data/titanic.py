import pandas as pd

import csv

titanic = pd.read_csv("pandas/data/titanic.csv")

# print(titanic)

# I want to see the first 8 rows of a pandas DataFrame.
# print(titanic.head(8))

# Get the last 5 rows of a DataFrame.
# print(titanic.tail(5))


# Display the shape and data types of the titanic DataFrame.
print(titanic.shape)
# print(titanic.dtypes)
