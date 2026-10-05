import os
import json

user_details = {"name": "sowmya", "age": 25, "designation": "Teacher"}

with open("users.json", mode="w") as f:
    data = json.dump(user_details, f, indent=3)

with open("users.json", mode="r") as f:
    result = json.load(f)

    print(f"user_details: {result}")

    print(result["designation"])
