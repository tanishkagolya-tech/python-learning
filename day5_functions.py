# Example 1 - simple function
def greet():
    print("Hello! Welcome to Python learning")
greet()

# Example 2 - function with parameters
def greet_user(name):
    print("Hello", name)
greet_user("Tanishka")

# Example 3 - function with return
def add(a, b):
    return a + b
result = add(10, 5)
print(result)

# Example 4 - even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(7))

def check_Even_odd(num):
    if num % 2 == 0:
        return "Even"

    else:
        return "Odd"

print(check_even_odd(2))

# Example 5 - square of a number
def square(num):
    return num * num
print(square(4))

# Example 6 - voting eligibility
def check_voting(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible"
print(check_voting(20))

# Example 7 - grade calculator
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"
print(calculate_grade(82))

# Example 8 - shopping bill total
def calculate_bill(price, quantity):
    total = price * quantity
    return total
print(calculate_bill(50, 3))

# Example 9 - simple calculator
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        return a / b
    else:
        return "Invalid operation"

print(calculator(10, 5, "add"))
print(calculator(10, 5, "mul"))


# Example 10 - celsius to fahrenheit

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(25))

