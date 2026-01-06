# Example 1 - write to a file
file = open("notes.txt", "w")
file.write("Learning Python File Handling\n")
file.write("Day 8 practice\n")
file.close()
print("Data written to file")

# Example 2 - read from a file
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()


# Example 3 - append data
file = open("notes.txt", "a")
file.write("Appending new line\n")
file.close()
print("Data appended")

# Example 4 - student data save
file = open("students.txt", "w")
file.write("Name: Tanishka, Marks: 85\n")
file.write("Name: Riya, Marks: 78\n")
file.close()
print("Student data saved")

# Example 5 - read student records
file = open("students.txt", "r")
for line in file:
    print(line.strip())
file.close()

# Example 6 - expense tracker
expenses = [120, 250, 90, 300]
file = open("expenses.txt", "w")
for e in expenses:
    file.write(str(e) + "\n")
file.close()
print("Expenses saved to file")

# Example 7 - calculate total expense
file = open("expenses.txt", "r")
total = 0
for line in file:
    total += int(line.strip())
file.close()
print("Total expense:", total)

# Example 8 - using with statement
with open("report.txt", "w") as file:
    file.write("Weekly Report\n")
    file.write("Python practice completed\n")
print("Report generated")

# Mini Project - Daily Learning Log

def add_log(message):
    with open("daily_log.txt", "a") as file:
        file.write(message + "\n")

add_log("Day 8: Learned file handling in Python")
add_log("Practiced write, read and append operations")

print("Daily log updated")
