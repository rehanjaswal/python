x = int(input("enter a number between 1 and 10: "))

match (x):
    case 1:
        print("you won an iPhone 17")
    case 7:
        print("you won a Nikon DSLR")
    case 10:
        print("you won a World Cup Trophy")
    case _:
        print("better luck next time")
    