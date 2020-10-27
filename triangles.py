import time
import math

def hypo(a, b): # counts hypothenuse
   c = math.sqrt(a**2 + b**2)
   return c

def cath(c, a): # counts cathetus
   b = math.sqrt(c**2 - a**2)
   return b

def cath_cos(c, x): #counts cathetus with a known angle measured in degrees
    rad = math.radians(x) #converts the input in degrees to radians
    cos = math.cos(rad) #counts the cos of an angle
    cat = c * cos #counts the cathetus
    return cat

def cath_sin(c, x): #counts cathetus with a known angle measured in degrees
    rad = math.radians(x)  # converts the input in degrees to radians
    sin = math.sin(rad)  # counts the sin of an angle
    cat = c * sin  # counts the cathetus
    return cat



while True:
   action = str(input(
       " \n "
       "Choose an action, enter an appropriate number and press enter\n"
       "1 - count hypothenuse\n"
       "2 - count cathetus\n"
       "3 - count cathetus with cos\n"
       "4 - count cathetus with sin\n "
       " "





   ))
   if action == "1":
      a = float(input("Enter first cathetus: "))
      b = float(input("Enter second cathetus: "))
      res = hypo(a, b)
      print("The result is: " + str(res))
      time.sleep(2)
   elif action == "2":
       try:
            c = float(input("Enter hypothenuse: "))
            a = float(input("Enter cathetus: "))
            res = cath(c, a)
            print("The result is: " + str(res))
            time.sleep(2)
       except ValueError:
           print("It seems that hypothenuse is less than cathetus. Try again!")
           time.sleep(2)
   elif action == "3":
       c = float(input("Enter hypothenuse: "))
       x = float(input("Enter angle in degrees: "))
       res = cath_cos(c, x)
       print("The result is: " + str(res))
       time.sleep(2)
   elif action == "4":
       c = float(input("Enter hypothenuse: "))
       x = float(input("Enter angle in degrees: "))
       res = cath_sin(c, x)
       print("The result is: " + str(res))
       time.sleep(2)
   else:
       print("There is no such an action. Try again")
       time.sleep(2)

