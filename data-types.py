# DATA TYPES

# Primitive Data Types
# These are the fundamental building blocks used to store single pieces of data.

# Integers - int -  ( Whole numbers without a decimal point. They can be positive, negative, or zero.)
age = 31
temperature = -50

# Float - float - ( Numbers that contain a decimal point. )
pi = 3.1454
percentage = 79.08

# Booleans - bool - ( Represent one of two values: True or False. Notice that they must be capitalized in Python. They are often the result of comparisons )
is_login = True
is_fail = False
has_error = True
is_major = age >= 18

# Strings - str - ( sequences of text characters. You can define them using either single quotes or double quotes )
name = "nousu"
notification = "Hello, Nousu"


# Collection Data Types
# Collections store multiple values in a single variable. The type of bracket used defines the type of collection.

# List ( Ordered, mutable collections. Define using square brackets []. Use lists when you have an ordered sequence of items that you might want ot be add to, remove from, modify later )
users_data = ["nousu", "sowmya", "Himanshu", "pallavi"]

users_data.append("chitti")
print(users_data)  # Output ['nousu', 'sowmya', 'Himanshu', 'pallavi', 'chitti']

users_data[0] = "pinky"
print(users_data)  # Output ['pinky', 'sowmya', 'Himanshu', 'pallavi', 'chitti']


# Tuples ( Ordered, immutable (unchangeable) collections. Defined using parentheses (). Use tuples for data that should never change throughout the life of your program, like fixed geographic coordinates or database credentials. )
coordinates = (34.454, -54.876)
rgb_red = (255, 0, 0)

# coordinates[0] = 23.0000 -> This would throw an error!
coordinates[0] = 23.0000
print(coordinates)

# Dictionaries ( Unordered collections of key-value pairs. Defined using curly braces {} with colons : separating keys and values. Use dictionaries when you need to look up values by a specific label (like a real-world dictionary). )
user_data = {"name": "nousu", "age": 31, "is_Ui_Developer": True}

# access values using their keys
print(user_data["name"]) 

# Sets ( Unordered collections of unique items. Defined using curly braces {} without colons. Use sets when you want to mathematically compare groups (intersections, differences) or quickly remove duplicates from a list. )

user_ids = {101, 102, 103, 103, 103}

# Sets automatically remove duplicates
print(user_ids)  # Outputs: {101, 102, 103}

