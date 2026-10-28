import os
import csv

print("Current directory: ", os.getcwd())

with open("custom.csv", mode="w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["name", "village"])
    writer.writerow(["nousu", "lingampally"])
    writer.writerow(["sowmya", "nomula"])

with open("custom.csv", mode="r") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)

custom_csv_file = "csv_file.csv"

if not os.path.exists(custom_csv_file):

    with open("csv_file.csv", mode="w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(["name", "village"])
        writer.writerows(["nousu", "lingampally"])
        writer.writerows(["sowmya", "nomula"])

        print(f"File '{custom_csv_file}' just now created.")

    # with open(custom_csv_file, mode="r") as f:
    #     reader = csv.reader(f)

    #     for row in reader:
    #         print(row)

else:
    print(f"File '{custom_csv_file}' already exists.")
