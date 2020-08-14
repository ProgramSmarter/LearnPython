import random
list2 = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def funct():
        y = input("Type in your first move. (1-9)")
        x = y
        x = int(x)
        x -= 1
        list2[int(x)] = "X"
        if int(y) not in list:
            print("That's already been taken! Try again!")
        else:
            list.remove(y)
        print(list2[0:3])
        print(list2[3:6])
        print(list2[6:9])
        compchoicerandom = random.choice(list)
while len(list) > 0:     
    funct()
        


    
