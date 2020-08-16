x = int(input("Input number!"))
x += 1
d = 0
for different in range(1, x):
    print(different)
    for diff in range(different):
        diff += 1
        print(diff, end = '')
x -= 2
for different in range(x, 1, -1):
    print()   
    for diff in range(different):
        diff += 1
        print(diff, end = "")
        diff -= 1
print()
print(1)
