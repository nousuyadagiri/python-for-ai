import requests
import json

# res = requests.get("https://jsonplaceholder.typicode.com/users")

# data = res.json()

# print(res.status_code)

# try:
#     if res.status_code == 200:
#         for user_name in data:
#             print(user_name["name"])
#     else:
#         print("there is no such user data not available !")
# except Exception as e:
#     print("An error occurred !", e)


print("--- 2. POST Request (with Request Body) ---")
# Method: POST is used to send new data to the server (e.g., creating a new user or post).
post_url = "https://jsonplaceholder.typicode.com/users"

# Request Body: The data we want to send. We define it as a Python dictionary.
new_post_data = {
    "title": "Learning APIs",
    "body": "APIs are fun to learn!",
    "userId": 1,
}

# The 'json=' parameter automatically converts our dictionary to JSON format
# and sets the correct headers for us.
response_post = requests.post(post_url, json=new_post_data)

# Status Code 201 usually means "Created"
print(f"Status Code: {response_post.status_code}")
print("Response Data from server after creation:", response_post.json())
print()

res = requests.get("https://jsonplaceholder.typicode.com/users")
result = res.json()
# print(result)

with open("custom.json", mode="w") as f:
    data = json.dump(result, f, indent=2)
