#Empty dictionary
#students = {}

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
    }
#associate one value with another - keys on the left, values on the right

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student)
#by default iterates over the KEYS

#Print also the value using the name to index into the dictionary

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student])
    print(student, students[student], sep= ", ")
#Iterating over keys instead of numeric location!

#Compose a list of dictionaries to associate multiple things with a student
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"])
for student in students: 
    print(student["name"], student["house"])
for student in students: 
    print(student["name"], student["house"], student["patronus"], sep = ", ")
