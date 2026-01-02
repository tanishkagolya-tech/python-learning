01_for_basic.py
for i in range(1, 11):
    print(i)

02_for_list.py
#Example 2 – Iterate through a list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

#Example 3 – Real-life scenario: Shopping list
shopping_list = ["milk", "curd", "bread"]
for item in shopping_list:
    print(f"Buying {item}")

03_while_basic.py
#Example 1 – Count 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1

#Example 2 – Real-life scenario: Bank balance check
balance = 5000
withdraw = 1000
while balance >= withdraw:
    print(f"Withdrawing {withdraw}")
    balance -= withdraw
print(f"Remaining balance: {balance}")

04_do_while_emulate.py
count = 1
while True:
    print(f"Number is {count}")
    count += 1
    if count > 5:
        break

#Real-life scenario: ATM pin attempts
attempts = 0
max_attempts = 3
correct_pin = 1234

while True:
    pin = int(input("Enter PIN: "))
    attempts += 1
    if pin == correct_pin:
        print("Access granted")
        break
    elif attempts >= max_attempts:
        print("Card blocked")
        break
    else:
        print("Wrong PIN, try again")

05_nested_loops.py
#Example 1 – Multiplication table 1–3
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end=" ")
    print()

#Example 2 – Real-life scenario: Cinema seating
rows = 3
seats_per_row = 4

for row in range(1, rows+1):
    for seat in range(1, seats_per_row+1):
        print(f"Row {row} Seat {seat}", end=", ")
    print()

 06_break_continue.py
for i in range(1, 11):
    if i % 2 == 0:
        continue 
    if i > 7:
        break 
    print(i)

# Example 1 – Sum of digits (real-life: check number validity)
num = 1234
sum_digits = 0
for digit in str(num):
    sum_digits += int(digit)
print(f"Sum of digits: {sum_digits}")

# Example 2 – Pattern Printing (Stars)
for i in range(1, 6):
    print("*" * i)

# Example 3 – Prime numbers 1–20
for num in range(2, 21):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
