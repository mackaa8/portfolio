name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else: 
    print("Who?")
    
#Shorten
name = input("What's your name? ")

if name == "Harry" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else: 
    print("Who?")
    
#Keyword MATCH & CASE
name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:                 #Additional case with different name
        print("Who?")

#Within the MATCH statement we can do an equivalent of Harry or Hermione or Ron
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")