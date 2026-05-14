# In Python, a function is a block of reusable code that performs a specific task. Instead of writing the same code again and again, you can put it inside a function and call it whenever needed.

# 🔹 How to define a function

# You use the def keyword:

def function_name(parameters):
    # code block
#     return value
# function_name → name of the function
# parameters → inputs (optional)
# return → sends result back (optional)
# # 🔹 Example 1: Simple function
# def greet():
    print("Hello, welcome!")
# Calling the function:
# greet()

# Output:

# Hello, welcome!
# 🔹 Example 2: Function with parameters
def greet(name):
    print("Hello", name)
# Calling:
greet("Alice")

# Output:

# Hello Alice
# 🔹 Example 3: Function with return value
def add(a, b):
    return a + b
# Calling:
result = add(3, 5)
print(result)

# Output:

8
# 🔹 Example 4: Function with default parameter
def greet(name="Guest"):
    print("Hello", name)
# Calling:
greet()
greet("John")

# Output:

# Hello Guest
# Hello John
# 🔹 Why use functions?
# Avoid repeating code
# Make programs easier to read
# Break big problems into smaller parts
# Reuse code in different places