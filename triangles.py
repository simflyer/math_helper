import math

def hypo(a, b): # counts hypothenuse
   c = math.sqrt(a**2 + b**2)
   return c

def cath(c, a): # counts cathetus
   b = math.sqrt(c**2 - a**2)
   return b

while True:
   action = str(input("Что ты хочешь сделать? \n 1 - посчитать гипотенузу \n 2 - найти катет \n"))
   if action == "1":
      a = float(input("Введите значение первого катета"))
      b = float(input("Введите значение второго катета"))
      print(hypo(a, b))
   elif action == "2":
      c = float(input("Введите значение гипотенузы"))
      a = float(input("Введите значение катета"))
      print(cath(c, a))

