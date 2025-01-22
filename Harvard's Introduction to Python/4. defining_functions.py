#Making our own functions; define - creating a function
def hello():
    print("hello")

name = input("What's your name? ")
hello()
print(name)

def hello(to):
    print("hello,", to)

name = input("What's your name? ")
hello(name)

#Give parameter "to" a default value

def hello(to = "world"):
    print("hello,", to)

hello()
name = input("What's your name? ")
hello(name)

#If the programmer doesn't call hello function with an argument - there is a default value; 

#Organise the code
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to = "world"):
    print("hello,", to)

main()

#I want a function to "HAND ME BACK" a value
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n*n

main()