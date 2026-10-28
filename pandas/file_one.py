import pandas as pd


df = pd.DataFrame({
    "Name": [
        "Nousu","Sowmya","Pallavi"
    ],
    "Age": [
        12,23,
        34
    ],
    "Gender": [
        "F","M","F"
    ],
    "Email": [
        "nousu@gmail.com", "sowmya@gmail.com", "pallavi@gmail.com"
    ]
})

# print(df)

# series
# Each column in a DataFrame is a Series

# print(df["Age"])

# creating a series form scratch
ages = pd.Series([22,23,24], name="Age")
emails = pd.Series(["nousu@gmail", "sowmya@gmail", "pallavi@gmaily"], name="Emails")
address = pd.Series(["Nomula, H.NO: 2-45", "Lingampally, H.NO: 2-77"], name= "Address")

# print(ages)
# print(emails)
# print(address)
# print(df.describe())

# series
# print(ages.max())

# dataFrame
# print(df["Age"].max())