import time
import math
def root(a, b, c): #gets an input of square equation terms and counts the root
   d = b**2 - 4 * a * c
   x1 = (-b + math.sqrt(d))/2 * a
   x2 = (-b - math.sqrt(d))/2 * a
   return x1, x2


while True:
    try:
        a = float(input("Enter first term (a): "))
        if a == 0:
            print("It is not square equation, first term can`t be 0")
            time.sleep(2)
        else:
            b = float(input("Enter second term (b): "))
            c = float(input("Enter third term (c): "))
            res = root(a, b, c)
            print("Here is the result: " + str(res))
            time.sleep(2)
    except ValueError:
        print("This equation does not have root")
        time.sleep(2)
