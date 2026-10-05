# Control flow dictates the order in which a program executes instructions. Using Python as the standard, here is how each control flow mechanism works, illustrated through a unified theme: processing an e-commerce shopping cart.

# 1. Conditionals (if / elif / else)

# Conditionals allow a program to make decisions and execute specific blocks of code only if certain conditions are met.

# Example: Calculating shipping costs based on cart total.

cart_total = 19.99

if cart_total >= 40:
    print("Free shipping applied!")
elif cart_total >= 25:
    print("Shipping is $3.99")
else:
    print("Shipping is $7.99")

# 2. For Loops

# A for loop iterates over a sequence (like a list, string, or range) and executes a block of code for each item. It is best used when you know exactly how many items you need to process.

# Example: Applying tax to each item in a cart.

cart_items = [10.00, 23.40, 34]
tax_rate = 0.06
total_with_tax = 0

for item in cart_items:
    taxed_item = item * tax_rate
    total_with_tax += taxed_item

print(f"Total: ${total_with_tax}")  # Output Total: $4.0440000000000005

# 3. While Loops

# A while loop continues to execute a block of code as long as a specified condition remains True. It is ideal for situations where you do not know in advance how many iterations are needed.

# Example: Draining an order processing queue.

orders_to_process = 10

while orders_to_process > 3:
    print(f"Processing order... ({orders_to_process} left)")
    orders_to_process -= 1  # Crucial: update the condition to avoid an infinite loop

print("All orders processed!")  # Output


cookies_on_plate = 3

# The computer asks: Is 3 greater than 0? Yes!
while cookies_on_plate > 0:
    print("I ate a cookie!")

    # We must remove a cookie from the plate
    cookies_on_plate = cookies_on_plate - 1

# The loop ends when cookies_on_plate hits 0
print("My plate is empty. I am done eating.")


# 4. Comprehensions

# Comprehensions are a concise, Pythonic way to create a new sequence (like a list or dictionary) by filtering and transforming an existing sequence in a single line of code. It replaces the need for a multi-line for loop.

# Example: Extracting only the expensive items and applying a 10% discount.

prices = [34, 26, 78, 46, 45, 100]

discount = 0.60

# premium_discount = [price * discount for price in prices if price > 50]
for price in prices:
    if price > 50:
        premium_discount = price * discount
        print(f"Discounted price: ${premium_discount}")


# 5. Early Returns

# An early return is a design pattern used inside functions. Instead of nesting multiple if/else blocks to check for errors, you check for failure conditions first and return immediately if they fail. This keeps the "happy path" (the main logic) clean and un-nested.

# Example: Validating a checkout attempt.


def process_checkout(is_logged_in, cart_is_empty, payment_valid):
    # 1. Early returns for invalid states (Guard Clauses)
    if not is_logged_in:
        return "Error: User must log in first."

    if cart_is_empty:
        return "Error: Cannot checkout an empty cart."

    if not payment_valid:
        return "Error: Payment declined."

    # 2. The "Happy Path" (only reached if all checks above pass)
    # Database logic and order confirmation goes here
    return "Success: Order placed!"


# Testing an invalid state
print(process_checkout(is_logged_in=True, cart_is_empty=True, payment_valid=True))
# Output: Error: Cannot checkout an empty cart.
