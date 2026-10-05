"""
APIs in Python

This file explains the concepts of:
1. HTTP Methods (GET, POST, PUT, DELETE)
2. Endpoints
3. Headers
4. Authentication
5. Request Bodies
6. Status Codes
7. JSON Responses

Note: We use the 'requests' library to demonstrate API calls.
You might need to install it first: pip install requests
"""

import json
import sys

# Try to import requests, providing a helpful error if it's not installed
try:
    import requests
except ImportError:
    print("The 'requests' library is not installed.")
    print("Please run: pip3 install requests")
    sys.exit()

# ==========================================
# 1. HTTP Methods, 2. Endpoints & 7. JSON Responses
# ==========================================
print("--- 1. GET Request ---")
# Endpoint: The URL where the API is hosted.
# Here we use a free placeholder API to get a sample "post".
endpoint_url = "https://jsonplaceholder.typicode.com/posts/1"

# Method: GET is used to retrieve/read data from the server.
print(f"Fetching data from: {endpoint_url}")
response_get = requests.get(endpoint_url)

# 6. Status Codes: Every response comes with a status code.
# 200 means OK (Success).
print(f"Status Code: {response_get.status_code}") 

# 7. JSON Responses: APIs usually return data in JSON format.
# The .json() method parses this JSON text into a Python dictionary.
data = response_get.json()
print("Response Data (parsed as Python dictionary):")
print(data)
print(f"Title of the post: {data.get('title')}\n")


# ==========================================
# 5. Request Bodies & 1. POST Method
# ==========================================
print("--- 2. POST Request (with Request Body) ---")
# Method: POST is used to send new data to the server (e.g., creating a new user or post).
post_url = "https://jsonplaceholder.typicode.com/posts"

# Request Body: The data we want to send. We define it as a Python dictionary.
new_post_data = {
    "title": "Learning APIs",
    "body": "APIs are fun to learn!",
    "userId": 1
}

# The 'json=' parameter automatically converts our dictionary to JSON format
# and sets the correct headers for us.
response_post = requests.post(post_url, json=new_post_data)

# Status Code 201 usually means "Created"
print(f"Status Code: {response_post.status_code}")
print("Response Data from server after creation:", response_post.json())
print()


# ==========================================
# 3. Headers & 4. Authentication
# ==========================================
print("--- 3. Headers and Authentication ---")
# Headers: Extra hidden information sent with the request.
# Authentication: Proving who you are. A common way is sending a "Bearer token" in the headers.

# httpbin.org is a great free service for testing HTTP requests.
# The /bearer endpoint specifically checks if you sent a Bearer token.
auth_url = "https://httpbin.org/bearer"

# We define headers as a dictionary
headers = {
    "Authorization": "Bearer my_super_secret_token",
    "Accept": "application/json" # Telling the server we want JSON back
}

# Sending a GET request, but this time we attach our headers
response_auth = requests.get(auth_url, headers=headers)

print(f"Status Code: {response_auth.status_code}")
if response_auth.status_code == 200:
    print("Authentication successful!")
    print("Response:", response_auth.json())
else:
    print("Authentication failed.")
print()


# ==========================================
# Common HTTP Status Codes to Remember:
# ==========================================
# 200 OK: Request was successful.
# 201 Created: New resource was successfully created (common in POST requests).
# 400 Bad Request: The server didn't understand the request (often a typo or missing data in request body).
# 401 Unauthorized: You need to log in or provide a valid API key.
# 403 Forbidden: You are logged in, but don't have permission to do this specific action.
# 404 Not Found: The endpoint doesn't exist (e.g., wrong URL).
# 500 Internal Server Error: The server crashed or had an error on their end.
