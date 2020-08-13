x = 0

def funct(x):
  factorialheho = 1
  g = 0
  f = int(input("Give a number to me. "))
  for z in range (1, f + 1):
    factorialheho = factorialheho + z
  print(factorialheho)
  funct(x)
funct(x)