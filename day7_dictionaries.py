# Example 1 - simple dictionary
student = {
    "name": "Tanishka",
    "age": 20,
    "course": "B.Tech"
}
print(student)

# Example 2 - access values
print(student["name"])
print(student["course"])

# Example 3 - loop through dictionary
for key, value in student.items():
    print(key, ":", value)


# Example 4 - update dictionary
student["age"] = 21
student["college"] = "ABC College"
print(student)

# Example 5 - student marks
marks = {
    "Maths": 85,
    "Science": 78,
    "English": 90
}

total = 0
for m in marks.values():
    total += m

average = total / len(marks)
print("Total:", total)
print("Average:", average)

# Example 6 - pass/fail per subject

for subject, mark in marks.items():
    if mark >= 40:
        print(subject, "Pass")
    else:
        print(subject, "Fail")# Example 7 - phone book

phone_book = {
    "Aman": 9000000000,
    "Riya": 9888888888,
    "Tanishka": 8000000000
}

name = "Tanishka"

if name in phone_book:
    print("Number:", phone_book[name])
else:
    print("Contact not found")


# Example 8 - expense tracker

expenses = {
    "food": 1200,
    "travel": 800,
    "shopping": 1500
}

total_expense = sum(expenses.values())
print("Total expense:", total_expense)

# Mini Project - Student Report System

student = {
    "name": "Tanishka",
    "marks": {
        "Maths": 85,
        "Science": 78,
        "English": 90,
        "Computer": 95
    }
}

total = 0
for m in student["marks"].values():
    total += m

average = total / len(student["marks"])

print("Name:", student["name"])
print("Total Marks:", total)
print("Average:", average)

if average >= 75:
    print("Grade: A")
elif average >= 50:
    print("Grade: B")
else:
    print("Grade: C")
