import random
def all():
    list2 = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    def funct():
            y = input("Type in your move. (1-9)")
            x = y
            y = int(y)
            y -= 1
            x = int(x)
            if int(y) not in list:
                print("That didn't work! Try again!")
                funct()
            else:
                list.remove(int(y))
                x -= 1
                list2[int(x)] = "X"
            print(list2[0:3])
            print(list2[3:6])
            print(list2[6:9])
            compchoicerandom = random.choice(list)
            compchoicerandom = int(compchoicerandom)
            list2[compchoicerandom] = 'O'
            list.remove(int(compchoicerandom))
            print("I've made my move!")
            if list2[0] and list2[1] and list2[2] == "O" or list2[3] and list2[4] and list2[5] == "O" or list2[6] and list2[7] and list2[8] == "O" or list2[0] and list2[3] and list2[6] == "O" or list2[1] and list2[4] and list2[7] == "O" or list2[2] and list2[5] and list2[8] == "O" or list2[0] and list2[4] and list2[8] == "O" or list2[2] and list2[4] and list2[6] == "O":
                print("You have won! :)")
                all()
            else:
                funct()
            if list2[0] and list2[1] and list2[2] == "X" or list2[3] and list2[4] and list2[5] == "X" or list2[6] and list2[7] and list2[8] == "X" or list2[0] and list2[3] and list2[6] == "X" or list2[1] and list2[4] and list2[7] == "X" or list2[2] and list2[5] and list2[8] == "X" or list2[0] and list2[4] and list2[8] == "X" or list2[2] and list2[4] and list2[6] == "X":
                print("You have lost! :(")
                all()
            else:    
                funct()
            if len(list) == 0:
                print("The game has ended in a draw!")
                all()
            else:
                funct()
    while len(list) > 0:     
        funct()
all()
        
