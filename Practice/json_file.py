import os
import json

user_details = {"name": "sowmya", "age": 25, "designation": "Teacher"}

if os.path.exists("Practice/users.json"):
    with open("Practice/users.json", mode="r") as f:
        result = json.load(f)

        print(result["designation"])
    print("File is already exists : ", os.path.exists("Practice/users.json"))
else:
    print("File is not exists : ", os.path.exists("Practice/users.json"))
    with open("Practice/users.json", mode="w") as f:
        data = json.dump(user_details, f, indent=3)
    print("File is created successfully.")


