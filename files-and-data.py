import json
import csv
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# File I/O and environment handling are foundational to managing application data and runtime configuration in Python.

# Plain Text Files (.txt)
# Always manage files using Python's with statement (context manager) to ensure file handles close automatically, and explicitly declare encoding="utf-8".

# with open("my_notes.txt", mode="w") as f:
#     f.write("I am deleting the previous data and simultaneously adding the new text!")

# with open("my_notes.txt", mode="a") as f:
#     f.write("Nousu is a UI Developer and learning the AI Engineering concepts!")

# with open("my_notes.txt", mode="r") as f:
#     matter = f.read()
#     print(matter)

# with open("my_custom_file", mode="w") as f:
#     f.write("New Data arrived!")
# with open("my_custom_file", mode="a") as f:
#     f.write(" OK and Thank you!")
# with open("my_custom_file", mode="r") as f:
#     para = f.read()
#     print(para)


# JSON FILES

# employee = {
#     "name": "nousu",
#     "age": 31,
#     "designation": "UI Developer",
#     "email": "nousuyadagiri20@gmail.com",
#     "has_driving_license": True,
# }

# with open("employee.json", mode="w") as f:
#     json.dump(employee, f)

# with open("employee.json", mode="r") as f:
#     data = json.load(f)
#     print(data["email"])

# user = {"name": "user", "is_admin": True, "role": "FrontEnd Developer"}

# with open("employee.json", mode="a") as f:
#     json.dump(user, f)
# with open("employee.json", mode="r") as f:
#     result = json.load(f)


# CSV FILES

# # writing
# with open("friends.csv", mode="w", newline="") as f:
#     writer = csv.writer(f)

#     # table heading
#     writer.writerow(["name", "village"])

#     # details
#     writer.writerow(["nousu", "lingampally"])
#     writer.writerow(["sowmya", "nomula"])

# # read
# with open("friends.csv", mode="r") as f:
#     reader = csv.reader(f)

#     for row in reader:
#         print(row)


# my_file = Path("friends.csv")
# print(my_file.exists())

# new_file = Path("hello.py")
# print(new_file.exists())


# api_key = os.environ.get("API_KEY", "default_value")
# database_url = os.environ.get("DATABASE_URL", "default_value")
# secret_key = os.environ.get("SECRET_KEY", "default_value")


# print(f"API Key: {api_key}")
# print(f"Database URL: {database_url}")
# print(f"Secret_Key: {secret_key}")
