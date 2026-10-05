# \"\"\"
# Errors and Debugging in Python

# This file contains examples and explanations for:
# 1. Exceptions
# 2. Tracebacks
# 3. Defensive checks
# 4. Logging
# 5. Simple tests

# Read the comments and run the code to understand how each concept works.
# \"\"\"

import logging
import traceback

# ==========================================
# 1. Exceptions & 2. Tracebacks
# ==========================================
# Exceptions are errors that occur during the execution of a program.
# Tracebacks show the exact sequence of function calls that led to the error.

def divide_numbers(a, b):
    # This try-except block helps us handle errors gracefully
    # instead of the program crashing abruptly.
    try:
        result = a / b
        print(f"Result: {result}")
        return result
    except ZeroDivisionError as e:
        # This block catches the specific error when dividing by zero.
        print("Error: You cannot divide a number by zero!")
        
        # We can also print the traceback to see exactly where it happened
        # This is very helpful for debugging complex programs.
        print("--- Traceback Details ---")
        traceback.print_exc()
        print("-------------------------")
    except TypeError as e:
        # This catches errors when wrong types are used (e.g., dividing string by number)
        print(f"Error: Invalid input types. Please provide numbers. Details: {e}")

print("--- Testing Exceptions ---")
divide_numbers(10, 2)   # Works fine
divide_numbers(10, 0)   # Triggers ZeroDivisionError and prints traceback
divide_numbers(10, "a") # Triggers TypeError
print()


# ==========================================
# 3. Defensive Checks
# ==========================================
# Defensive programming means checking inputs or states to prevent errors early.
# 'assert' is commonly used for this. If the condition is false, it raises an AssertionError.

def calculate_discount(price, discount_percent):
    # Defensive check: Make sure price is not negative
    assert price >= 0, "Price cannot be negative"
    
    # Defensive check: Make sure discount is between 0 and 100
    if not (0 <= discount_percent <= 100):
        raise ValueError("Discount must be between 0 and 100")
        
    final_price = price - (price * (discount_percent / 100))
    return final_price

print("--- Testing Defensive Checks ---")
print(f"Discounted price: {calculate_discount(100, 20)}") # Works fine

try:
    calculate_discount(-50, 10) # Fails the assertion check
except AssertionError as e:
    print(f"Assertion Error Caught: {e}")

try:
    calculate_discount(100, 150) # Fails the ValueError check
except ValueError as e:
    print(f"Value Error Caught: {e}")
print()


# ==========================================
# 4. Logging
# ==========================================
# Logging is better than print() because you can control the output level
# (DEBUG, INFO, WARNING, ERROR, CRITICAL) and save logs to a file.

# Configure basic logging setup
logging.basicConfig(
    level=logging.DEBUG, # Set to DEBUG to see all messages
    format='%(asctime)s - %(levelname)s - %(message)s'
)

print("--- Testing Logging ---")
def process_data(data):
    logging.info("Starting data processing")
    
    if not data:
        logging.warning("Data is empty. Nothing to process.")
        return
        
    for item in data:
        logging.debug(f"Processing item: {item}")
        if type(item) is not int:
            logging.error(f"Invalid data type found: {item}. Skipping.")
            continue
            
    logging.info("Finished data processing")

process_data([1, 2, "apple", 4])
print()


# ==========================================
# 5. Simple Tests
# ==========================================
# Tests ensure your code works exactly as expected.
# You can write simple tests using assert statements.

def add(a, b):
    return a + b

def test_add_function():
    # If the condition is true, nothing happens.
    # If it's false, the program will throw an AssertionError.
    assert add(2, 3) == 5, "Test failed: 2 + 3 should be 5"
    assert add(-1, 1) == 0, "Test failed: -1 + 1 should be 0"
    assert add(0, 0) == 0, "Test failed: 0 + 0 should be 0"
    print("All tests passed successfully!")

print("--- Running Simple Tests ---")
test_add_function()
print()
