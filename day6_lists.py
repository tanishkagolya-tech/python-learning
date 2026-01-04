# Example 1 - simple list

numbers = [1, 2, 3, 4, 5]
print(numbers)

# Example 2 - access list elements

fruits = ["apple", "banana", "mango"]

print(fruits[0])
print(fruits[1])

# Example 3 - loop with list

marks = [70, 85, 60, 90]

for m in marks:
    print(m)

# Example 4 - total and average marks

marks = [70, 85, 60, 90]
total = sum(marks)
average = total / len(marks)
print("Total:", total)
print("Average:", average)

# Example 5 - pass or fail list

marks = [35, 78, 45, 20]

for m in marks:
    if m >= 40:
        print(m, "Pass")
    else:
        print(m, "Fail")

  # Example 6 - count pass students

def count_pass(marks):
    count = 0
    for m in marks:
        if m >= 40:
            count += 1
    return count

marks = [35, 78, 45, 20, 60]
print("Pass students:", count_pass(marks))

# Example 7 - find maximum

numbers = [10, 45, 3, 99, 23]

print("Maximum:", max(numbers))

# Example 8 - shopping cart total

prices = [199, 299, 149, 99]

def cart_total(prices):
    total = 0
    for p in prices:
        total += p
    return total

print("Total bill:", cart_total(prices))

# Example 9 - attendance system

attendance = [1, 0, 1, 1, 0, 1]   # 1 = present, 0 = absent

present = 0
absent = 0

for a in attendance:
    if a == 1:
        present += 1
    else:
        absent += 1

print("Present:", present)
print("Absent:", absent)

# Example 10 - highest marks

marks = [45, 78, 89, 60, 72]

highest = marks[0]

for m in marks:
    if m > highest:
        highest = m

print("Highest marks:", highest)

# Example 11 - filter passed students

marks = [35, 78, 45, 20, 60]
passed = []

for m in marks:
    if m >= 40:
        passed.append(m)

print("Passed marks:", passed)

# Example 12 - expense tracker

expenses = [120, 250, 90, 300, 60]

total = 0
for e in expenses:
    total += e

print("Total expense:", total)

# Example 13 - average using function

def calculate_average(values):
    total = 0
    for v in values:
        total += v
    return total / len(values)

marks = [70, 85, 60, 90]
print("Average marks:", calculate_average(marks))


# Example 14 - salary increment

salaries = [15000, 22000, 18000, 30000]
updated_salaries = []

for s in salaries:
    updated_salaries.append(s + 2000)

print("Updated salaries:", updated_salaries)


# Example 15 - search in list

names = ["Aman", "Riya", "Tanishka", "Rahul"]

search_name = "Tanishka"
found = False

for name in names:
    if name == search_name:
        found = True

if found:
    print(search_name, "found in list")
else:
    print(search_name, "not found")

