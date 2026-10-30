"""
Advanced Python Functions Tutorial
----------------------------------
Exploring Variable Scope, Recursion, and First-Class Functions.
"""

# ==========================================
# 1. Variable Scope (LEGB Rule)
# ==========================================
# Scope determines where a variable is accessible in your code.
# Local Scope: Variables defined inside a function.
# Global Scope: Variables defined at the top level of a script.

global_var = "I am global"

def check_scope():
    local_var = "I am local"
    print(global_var)  # Accessible
    print(local_var)   # Accessible

check_scope()
# print(local_var)  # Error! local_var is not accessible outside the function.


# ==========================================
# 2. Recursion
# ==========================================
# A recursive function is a function that calls itself to solve a smaller piece 
# of the same problem. Every recursive function needs a "base case" to stop.

def countdown(n):
    """Recursively counts down from n to 0."""
    # Base case: stop when n reaches 0
    if n <= 0:
        print("Blast off! 🚀")
        return
    
    print(n)
    # Recursive call with a smaller problem
    countdown(n - 1)

print("--- Recursion Example ---")
countdown(3)


# ==========================================
# 3. First-Class Functions & Higher-Order Functions
# ==========================================
# In Python, functions are treated like any other object (variables, strings, ints).
# You can assign them to variables, pass them as arguments, and return them.

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

# Higher-order function: accepts another function as an argument
def greet_with_style(func, message):
    """Applies a formatting function to a message and prints it."""
    result = func(message)
    print(result)

print("\n--- Higher-Order Function Example ---")
greet_with_style(shout, "hello world")    # Output: HELLO WORLD
greet_with_style(whisper, "HELLO WORLD")  # Output: hello world