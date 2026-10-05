# A function is a self-contained block of code designed to perform a single, specific task. By isolating logic into functions, you write code once and reuse it indefinitely, preventing duplication and making large systems manageable.

# Think of a function as a specialized machine in a factory. You feed raw materials into one end, the machine performs a specific task, and a finished product comes out the other end.
# In programming, this "machine" allows you to write a piece of code once and use it thousands of times without rewriting it.
# Here is a breakdown of how the different parts of a function work, using Python as the example language.


# 1. Parameters (The Inputs)
# Parameters are the slots on your machine where you insert the raw materials. They allow functions to be flexible so they can handle different data each time you run them.

# Imagine a digital greeting machine. Instead of building a new machine for every person on Earth, you build one machine with a slot (parameter) for a name.


def greet_person(name):  # 'name' is the parameter
    print(f"Hello, {name}!")


# Using the function with different inputs:
greet_person("Alice")  # Outputs: Hello, Alice!
greet_person("Bob")  # Outputs: Hello, Bob!


# 2. Return Values (The Outputs)
# Printing something to a screen just displays it. A return value is the machine actually handing the finished product back to you so you can use it in the next step of your assembly line.

# Once a function hits a return statement, it immediately stops and hands the data back.


def calculate_tax(price):
    tax = price * 0.20
    return tax  # Hands the value back to the program


# We can save the returned value into a variable
shoe_tax = calculate_tax(100)
print(shoe_tax)  # Outputs: 20.0


# 3. Type Hints (The Warning Labels)
# Type hints are sticky notes you put on the machine's input slots and output chute. They tell other programmers (and your computer's editor) exactly what type of data should go in and what will come out. They don't change how the code runs, but they prevent silly mistakes—like trying to do math on a word.


# The hints: 'price' should be a float (decimal), and it returns a float
def calculate_tax(price: float) -> float:
    return price * 0.20


# 4. Scope (The One-Way Mirror)
# Scope is the rule of "what happens inside the function, stays inside the function."

# Variables created inside a function are local. They are born when the function starts and destroyed when the function ends. The rest of your program cannot see or touch them.

global_password = "OpenSesame"  # Everyone can see this


def my_function():
    secret_code = "1234"  # Local variable
    print(global_password)  # Functions CAN see outside variables


my_function()
print(secret_code)  # ERROR! The outside program cannot see inside the function.


# 5. Reusable Modules (The Tool Shed)
# Eventually, you will write a lot of useful functions. Instead of copying and pasting them into every new project, you can save them in a separate file called a module.

# You can then import that file into any new project, just like pulling a tool out of a shed.


# Step 1: Save a file named math_tools.py
def add(a, b):
    return a + b


# Step 2: Use it in a totally different file
import math_tools

result = math_tools.add(5, 10)
print(result)  # Outputs: 15

