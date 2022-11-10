1# This is the mini-project
# File Name     : mainMenu.py
# Date          : 22 Oct 2022
# Modify Date   : 04 Nov 2022 (week3)
# Developer     : Samuel KO
# Description   : Build a Main Menu
#               : 1) Go to product menu
#               : 2) Go to order menu
#               : 3) Go to couriers menu
#               : 0) Exit the entire app/system

import sys
import os
import prodStorage

# Loading products, couriers, and order data
from productMenu import *
from orderMenu import *
from courierMenu import *

def mainMenu():
    keepOn = True
    os.system("clear")

    while keepOn:
            print("_________________________")
            print("_ Welcome to CLI system _")
            print("_                       _")
            print("_  1)--Product Menu     _")
            print("_  2)--Courier Menu     _")
            print("_  3)--Order Menu       _")
            print("_  0)--Exit System      _")
            print("_________________________")
            print(" ")
            try:
                choice = input("Please enter your choice :- ")
                if (choice.isdigit()):
                    choice = int(choice)
                    pass
                else:
                    print("Oops, wrong input of \'" + choice + "\' !!!! Enter again please.")
                    continue
                
                if choice in range(0, 4):
                    if (choice == 0):
                        # Save products list
                        # Save couriers list
                        print("Good, you want to exit the system, see you next time~")
                        keepOn = False
                    elif (choice == 1):
                         productMenu()
                    elif (choice == 2):
                         courierMenu()
                    elif (choice == 3):
                         orderMenu()
                else:
                    print("Input a wrong selection, try input again!")
                    continue
            except:
                print(f"Invalid choice of {choice}")
                continue
mainMenu()