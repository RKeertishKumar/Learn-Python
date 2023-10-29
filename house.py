name = input("What's your name? ")

match name:
    case "Harry" | "Ron":
        print("Gryiffindor")
        
    case "Draco":
        print("Slytherin")
        
    case _:
        print("Who?")