import random
def all():
    list2 = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    def funct():
            x = input("Type in your move. (1-9)")
            x = int(x)
            x -= 1
            if x not in list:
                print("That didn't work! Try again!")
                funct()
            else:
                list.remove(x)
                list2[x] = "X"
            print(list2[0:3])
            print(list2[3:6])
            print(list2[6:9])
            if (list2[0] and list2[1] and list2[2] == "O" == True) or (list2[3] and list2[4] and list2[5] == "O" == True) or (list2[6] and list2[7] and list2[8] == "O" == True) or (list2[0] and list2[3] and list2[6] == "O" == True) or (list2[1] and list2[4] and list2[7] == "O" == True) or (list2[2] and list2[5] and list2[8] == "O" == True) or (list2[0] and list2[4] and list2[8] == "O" == True) or (list2[2] and list2[4] and list2[6] == "O" == True):
                print("You have won! :)")
                all()
            else:
                pass
            if (list2[0] and list2[1] and list2[2] == "X") or (list2[3] and list2[4] and list2[5] == "X") or (list2[6] and list2[7] and list2[8] == "X") or (list2[0] and list2[3] and list2[6] == "X") or (list2[1] and list2[4] and list2[7] == "X") or (list2[2] and list2[5] and list2[8] == "X") or (list2[0] and list2[4] and list2[8] == "X") or (list2[2] and list2[4] and list2[6] == "X") or ():
                print("You have lost! :(")
                all()
            else:    
                pass
            if len(list) == 0:
                print("The game has ended in a draw!")
            else:
                pass
            compchoicerandom = int(random.choice(list))
            list2[compchoicerandom] = 'O'
            list.remove(int(compchoicerandom))
            print("I've made my move!")
            print(list2[0:3])
            print(list2[3:6])
            print(list2[6:9])
            if (list2[0] and list2[1] and list2[2] == "O" == True) or (list2[3] and list2[4] and list2[5] == "O" == True) or (list2[6] and list2[7] and list2[8] == "O" == True) or (list2[0] and list2[3] and list2[6] == "O" == True) or (list2[1] and list2[4] and list2[7] == "O" == True) or (list2[2] and list2[5] and list2[8] == "O" == True) or (list2[0] and list2[4] and list2[8] == "O" == True) or (list2[2] and list2[4] and list2[6] == "O" == True):
                print("You have lost! :)")
                all()
            else:
                pass
            if (list2[0] and list2[1] and list2[2] == "X") or (list2[3] and list2[4] and list2[5] == "X") or (list2[6] and list2[7] and list2[8] == "X") or (list2[0] and list2[3] and list2[6] == "X") or (list2[1] and list2[4] and list2[7] == "X") or (list2[2] and list2[5] and list2[8] == "X") or (list2[0] and list2[4] and list2[8] == "X") or (list2[2] and list2[4] and list2[6] == "X"):
                print("You have won! :(")
                all()
            else:    
                pass
            if len(list) == 0:
                print("The game has ended in a draw!")
            else:
                funct()
    while len(list) > 0:     
        funct()
all()
        
