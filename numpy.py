x = range(int(input("Give me how many numbers you want to multiply.")))
list = []
for s in x: list.append(int(input("Type in a number. ")))
y = 1
for z in list:  y *= z
print(y)