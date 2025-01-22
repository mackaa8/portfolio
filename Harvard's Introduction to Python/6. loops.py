print("meow")
print("meow")
print("meow")

#Keyword WHILE for creating a loop
#i = 3
#while i != 0:
    #print("meow")
#INFINITE LOOP (ctrl+c - a way to escape)

i = 3
while i != 0:
    print("meow")
    i = i -1 
#On each iteration we are decreasing i by 1 until it reaches 0 

i = 0 
while i <= 3:
    print("meow")
    i = i + 1
#Program "meows" 4 times because we start at 0 and we include 3!

#FOR loops - allow you to iterate over a list of items!
for i in[0,1,2]:
    print("meow")

#We should use a function to specify the values rather than listing them
#Function RANGE returns a range of values
for i in range(3):
    print("meow")

#We shouldn't be creating a variable 'i' that we are not later using - name this variable with a single underscore
for _ in range(3):
    print("meow") 

print("meow" * 3)

print("meow\n" * 3)

print("meow\n" * 3, end = "")

#Ask the user how many times the cat should meow and avoid the user putting a negative number
while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break
for _ in range(n):
    print("meow")

while True: 
    n = int(input("What's n? "))
    if n > 0:
        break
for _ in range(n):
    print("meow")
    
#Creating a function to print "meow" 3 times
def main():
    meow(3)

def meow(n):
    for _ in range(n):
        print("meow")

main()

#Creating a function to print "meow" n times
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0: 
            return n 
    
def meow(n):
    for _ in range(n):
        print("meow")

main()