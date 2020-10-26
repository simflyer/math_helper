import math

def hypo(a, b): # counts hypothenuse
   c = math.sqrt(a**2 + b**2)
   return c

def cath(c, a): # counts cathetus
   b = math.sqrt(c**2 - a**2)
   return b

def cath_cos(c, x): #counts cathetus with a known angle measured in degrees
    rad = math.radians(x) #converts the output in degrees to radians
    cos = math.cos(x) #counts the cos of an angle
    cat = c * cos #counts the cathetus
    return a



while True:
   action = str(input(
       "Choose an action, print an appropriate number and press enter\n"
       "1 - count hypothenuse\n"
       "2 - count cathetus\n"
       "3 - count cathetus with known cos"





   ))
   if action == "1":
      a = float(input("Enter first cathetus"))
      b = float(input("Enter second cathetus"))
      print(hypo(a, b))
   elif action == "2":
      c = float(input("Enter hypothenuse"))
      a = float(input("Enter cathetus"))
      print(cath(c, a))
   elif action == "3":
       c = float(input("Enter hypothenuse"))

