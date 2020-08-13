def funct():
    x = int(input("Type in a integer!"))
    print(x)
    if (x % 2) == 0:
        print("Your integer is even.")
    else:
        print("Your integer is odd.")
    y = str(input("Play Again? Print y for yes or n for no"))
    if y == "y":
        funct()
    if y == "n":
        exit() 
funct()      
        