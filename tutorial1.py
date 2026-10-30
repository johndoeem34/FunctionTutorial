"""
Python Functions Tutorial: Beginner to Intermediate
"""

# ==========================================
# 1. Basic Functions
# ==========================================
# A function is a reusable block of code that performs a specific task.
# Use the `def` keyword followed by the function name and parentheses.

def greet_user(name):
    """A simple function that takes one parameter and prints a greeting."""
    print(f"Hello, {name}! Welcome to the Python functions tutorial.")


greet_user("Alice")


# ==========================================
# 2. Returning Values
# ==========================================
# Functions can send data back using the `return` keyword. 
# Once a `return` statement is executed, the function exits.

def add_numbers(a, b):
    """Takes two numbers and returns their sum."""
    return a + b

result = add_numbers(5, 7)
print(f"5 + 7 = {result}")


# ==========================================
# 3. Default Arguments & Keyword Arguments
# ==========================================
# You can assign default values to parameters. If no argument is passed, the default is used.

def describe_pet(pet_name, animal_type="dog"):
    """Displays information about a pet with a default animal type."""
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("Buddy")                    # Uses default animal_type="dog"
describe_pet("Whiskers", animal_type="cat") # Overrides default


# ==========================================
# 4. Arbitrary Arguments (*args and **kwargs)
# ==========================================
# Use *args to pass a variable number of positional arguments (packed into a tuple).
# Use **kwargs to pass a variable number of keyword arguments (packed into a dictionary).

def calculate_total(*prices, tax_rate=0.05):
    """Sums up any number of item prices and applies an optional tax rate."""
    subtotal = sum(prices)
    total = subtotal + (subtotal * tax_rate)
    return total

print(f"Total price: ${calculate_total(10.99, 5.49, 3.25):.2f}")


# ==========================================
# 5. Lambda Functions (Anonymous Functions)
# ==========================================
# Small, one-line functions defined using the `lambda` keyword.

# Standard function
def square(x):
    return x * x

# Equivalent lambda function
square_lambda = lambda x: x * x

print(f"Square of 6 using lambda: {square_lambda(6)}")