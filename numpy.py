
def funct():
  x = int(input("Give me how many numbers you want to multiply."))
  list = []
  y = 0
  while y < x:
    list.append(int(input("Type in a number. ")))
    y += 1
  y = 1
  for z in list:
    y *= z
  print(y)
  funct()
      

    
  
funct()