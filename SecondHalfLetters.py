def secondhalfletters():
    floof = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    x = str(input("Give me a word."))
    x = x.lower()
    y = 0
    for z in x:
        if z in floof:
            y += 1
    print("There are " + str(y) + " letters in your name that are in the second half of the alphabet.")
secondhalfletters()

