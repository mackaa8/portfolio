#We can modify our strings (types of data) by using different functions

#Ask user for their name
name = input("What's your name? ")

#Say hello to user
print(f"hello, {name}")

#Solution if we accidentally put too many spaces before the name input

#Ask user for their name
name = input("What's your name? ")

#Remove whitespace from str
name = name.strip()

#Say hello to user
print(f"hello, {name}")

#Capitalize user's name
#Ask user for their name
name = input("What's your name? ")

#Remove whitespace from str
name = name.strip()

#Capitalize user's name
name = name.capitalize()

#Say hello to user
print(f"hello, {name}")

#We can use TITLE function that capitalizes first letter of each word
name = input("What's your name? ")
#Remove whitespace from str
name = name.strip()

#Capitalize user's name
name = name.title()

print(f"hello, {name}")

#Works, but too many lines of code for such and easy action concerning only ONE VARIABLE
#Ask user for their name
name = input("What's your name? ")

#Remove whitespace from str AND capitalize user's name
name = name.strip().title()

#Say hello to user
print(f"hello, {name}")

#SIMPLIFY
name = input("What's your name? ").strip().title()

#Say hello to user
print(f"hello, {name}")

#SPLIT user's name into first & last
name = input("What's your name? ").strip().title()

#Split user's name 
first, last = name.split(" ")
#splitting between the space character and assigning left to the "first" variable and right to the "last" variable 

#Say hello to user 
print(f"hello, {name}")


