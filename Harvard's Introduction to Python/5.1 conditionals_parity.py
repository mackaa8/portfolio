x = int(input("What's x? "))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

#Bool - type of data that can only be True or False
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else: 
        print("Odd")

#This function is a Boolean expression - because it returns either True or False
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()

#Improve and shorten
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False

main()

#IMPROVE
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else: 
        print("Odd")

def is_even(n):
    return n % 2 == 0 

main()