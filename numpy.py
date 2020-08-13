def funct():
    global x
    x = []
    if x[1] == "h" or x[1] == "H":
      Suit = " of Hearts"
      number()
    elif x[1] == "c" or x[1] == "C":
      Suit = " of Clubs"
      number()
    elif x[1] == "D" or x[1] == "d":
      Suit = " of Diamonds"
      number()
    elif x[1] == "S" or "s":
      Suit = " of Spades"
      number()
    funct()
def number():
  y = range(1, 10)
  if x in y:
    f = "Your card is {}" + Suit
    print(f.format(x))
funct()



    

      


