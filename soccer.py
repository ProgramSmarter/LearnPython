import os
s = 5  #s is now of type int
def functionstuff(s):   
    if s == 1:
        f = open("text.txt", "r")
        print(f.read())
        
    elif s == 2:
        y = open("text.txt", "a")
        b = input("What would you like to add to the list? ")
        y = open("text.txt", "a")
        y.write('\n')
        y.write(b)
        y.close()
       
    elif s == 3:
        y = open("text.txt", "r")
        y = open("text.txt", "w")
        y.write("Soccer Supplies are: ")
        y.close()
        
    elif s == 4:
        h = input("What would you like to remove?")
        with open("text.txt", "r")  as f:
            alllines = f.readlines()
        with open("text.txt", "w") as f:
            for line in alllines:
                if line.strip("\n") != h:  
                        f.write(line) 
        if h not in alllines: 
            print("I can't delete " + h + ", because it is not in the list!")
            functionlistsoccer()  
    
    
            

    else:
        print("Invalid Input! Try Again!!!!")
        

def functionlistsoccer():
    try:   
        s = int(input("What would you like to do? Type in 1 for the list, 2 to add something to it, 3 to reset the entire list, and 4 to remove something from the list. ")) 
        functionstuff(s)#call function functionstuff with parameter of s
    except: print("Try again! Invalid input!")

    finally: functionlistsoccer()
...         

functionlistsoccer()
