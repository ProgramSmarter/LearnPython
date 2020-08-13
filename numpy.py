def funct():
    x = input("Type in a color. r for red, g for green, and b for blue.")
    x.upper()
    print(x)
    if x == "R":
        print("Your color is red.")
        funct()
    elif x == "B":
        print("Your color is blue.")
        funct()
    elif x == "G":
        print("Your color is green.")
        funct()
    else:
        print("Invalid input! Try again!")
        funct()
funct()