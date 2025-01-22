students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])

#you can use a FOR LOOP to iterate over anything (not just numbers but strings)
students = ["Hermione", "Harry", "Ron"]

for student in students: 
    print(student)

#function LEN - tells you the lenght of a list
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(students[i])

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i, students[1])

#Not to start counting at 0!

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])

