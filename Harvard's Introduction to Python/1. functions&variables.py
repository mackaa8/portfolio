print("hello, world")

print("What's your name? ")
input()
print("hello, world")

input("What's your name? ")
print("hello, world")

input("What's your name? ")
print("hello, David")

name = input("What's your name? ")
print("hello,")
print(name) 

#Ask user for their name 
name = input("What's your name? ")

#Say hello to user
print("hello,")
print(name)

#FIX this code
#Ask user for their name
name = input("What's your name? ")

#Say hello to user 
print("hello, " + name)

#Different approach (as 2 arguments)
name = input("What's your name? ")
print("hello,", name)   

#OVERWRITE the value pf the separator parameter
name = input("What's your name? ")
print("hello,", name, sep="???")

#Overwrite the end parameter - end is no longer a new line for this specific function
name = input("What's your name? ")
print("hello,", name, end=None)

#Saying hello + name - using a new feature of F STRINGS!/ the most frequent way of solving

#Ask user for their name
name = input("What's your name? ")

#Say hello to user
print(f"hello, {name}")






