x = 1 
y = 2 

z = x + y 

print(z)

x = input("What's x? ")
y = input("What's y? ")
z = x + y

print(z)
#PLUS operator joined the strings (eg. 1 + 2 = 12), even though the user typed a number! 

#Switch from strings to INTEGERS
x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)

#SIMPLIFY (combining two functions)
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x+y) 
#result of one function (input) becomes the input to another function (int); we get the integer of x value! 

#FLOATS - numbers with a decimal point (may also be a function)

x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y) 

#ROUND to the nearest integer
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(z)

#specify to format the number 1000 using a dot/coma - 1,000 / formatting the f string!

x = float(input("What's x? "))
y = float(input("What's y? " ))

z = round(x + y) 

print(f"{z:,}")

#Calculator - DIVISION
x = float(input("What's x? "))
y = float(input("What's y? ")) 

z = x/y

print(z)

#ROUND
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x /y, 2) #2 - number of digits to round to 
print(z)

#we cam also specify using an f string how many digits we want to print! /python documentation/ 

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x /y

print(f"{z:.2f}")

