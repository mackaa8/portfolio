#Create 3 stacked bricks 
print("#")
print("#")
print("#")

for _ in range(3):
    print("#")

#Create a function
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")
    
main()

#More complexed syntax
def main():
    print_column(3)

def print_column(height):
    print("#\n" * height, end = None)

main()

#Print a row of 4 question marks
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()

#Implement height + width
def main():
    print_square(3)

def print_square(size):

#For each row in square
    for i in range(size):
        #For each brick in row
        for j in range(size):
            #Print bricks
            print("#", end = None)
#print new line
    print()

main()

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size)

main()

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()