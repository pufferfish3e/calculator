# import math
import os
from sys import exit


def main():
   print("Calculator v1.0")
   print("Patch notes:\n BODMAS system has not been implemented, ",end="")
   print("so evaluation will be done from left to right")
   print("---------------------------")
   userChoice = input("1. Calculate\n2. Polynomial\n3.Trigonometry\n4. Settings\n5. Exit\n")
   if userChoice == "c" or userChoice == "1":
      os.system("clear")
      calculate(prevAnswer=0)
   elif userChoice == "p" or userChoice == "2":
      os.system("clear")
      polynomial()
   elif userChoice == "s" or userChoice == "3":
      os.system("clear")
      settings()
   elif userChoice == "e" or userChoice == "4":
      exit()
   else:
      os.system("clear")
      print("\ninvalid, please enter singular characters (e.g. calculator -> c\n\n")
      main()
      
def calculate(prevAnswer):
   userQuestion = input("Calculate?\n")
   if userQuestion == "exit":
      main()
   equation = []
   number = ""
   for char in userQuestion:
      if char.isdigit():
         number += str(char)
      elif char == "a":
         number += str(prevAnswer)
      else:
         equation.append(number)
         number = ""
         equation.append(char)
   equation.append(number)

   i = 0
   for args in equation:
      for i in range(len(equation)-1):
         try:
            if args == "+": 
               ans = float(equation[equation.index(args)-1]) + float(equation[equation.index(args)+1])
               equation.pop(equation.index(args)-1)
               equation.pop(equation.index(args)+1)
               equation.pop(equation.index(args))
               equation.insert(0+i,ans)
               i += 1 
            elif args == "-":
               ans = float(equation[equation.index(args)-1]) - float(equation[equation.index(args)+1])
               equation.pop(equation.index(args)-1)
               equation.pop(equation.index(args)+1)
               equation.pop(equation.index(args))
               equation.insert(0+i,ans)
               i += 1  
            elif args == "*":
               ans = float(equation[equation.index(args)-1]) * float(equation[equation.index(args)+1])
               equation.pop(equation.index(args)-1)
               equation.pop(equation.index(args)+1)
               equation.pop(equation.index(args))
               equation.insert(0+i,ans)
               i += 1  
            elif args == "/":
               ans = float(equation[equation.index(args)-1]) / float(equation[equation.index(args)+1])
               equation.pop(equation.index(args)-1)
               equation.pop(equation.index(args)+1)
               equation.pop(equation.index(args))
               equation.insert(0+i,ans)
               i += 1
         except ValueError:
            break
   
   print(equation[0])
   calculate(prevAnswer=equation[0])

def trigonometry():
   userQuestion = input("Calculate?\n")
   
   
def polynomial():
   pass

def settings():
   pass

main()
