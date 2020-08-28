x = int(input("Type in a number. "))
y = int(input("Type in another number. "))
z = int(input("Type in a final number. "))
if x < y < z:
    glob = ("The median of your three numbers is {}.")
    print(z.format(y))
if z < y < x:
    glob = ("The median of your three numbers is {}.")
    print(glob.format(y))
if y < x < z:
    glob = ("The median of your three numbers is {}.")
    print(glob.format(x))
if z < x < y:
    glob = ("The median of your three numbers is {}.")
    print(glob.format(x))
if y < z < x:
    glob = ("The median of your three numbers is {}.")
    print(glob.format(z))
if z < x < y:
    glob = ("The median of your three numbers is {}.")
    print(glob.format(z))

