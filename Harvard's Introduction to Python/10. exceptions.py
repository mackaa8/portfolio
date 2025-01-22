#Write code with errors in mind
#Keyword TRY and EXCEPT
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

#Keyword ELSE
try: 
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")


#Using a loop to prompt the user again&again to put an integer: 
while True: 
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else: 
        break

print(f"x is {x}")

#Another way to do that - organise your code differently
while True: 
    try: 
        x = int(input("What's x? "))
        break
    except ValueError: 
        print("x is not an integer") 
    
print(f"x is {x}")

#Write a function to get integer from user
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True: 
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else: 
            return x 
        
#Different approach
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
            return x
        except ValueError:
            print("x is not an integer")

main()

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")

    main()

#PASS keyword
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass

main()

#Make the code reusable
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try: 
            return int(input(prompt))
        except ValueError:
            pass

main()