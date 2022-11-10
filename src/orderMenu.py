# This is the mini-project
# File Name     : orderMenu.py
# Date          : 22 Oct 2022
# Developer     : Samuel KO
# Description   : Build a Order Menu
#               : 1) Print order dictionary
#               : 2) Add order
#               : 3) Update order
#               : 4) STRETCH update order
#               : 5) Delete order
#               : 0) Exit Order Menu

import sys
import os

# Set the global myProdList as global variable by 
# putting it to listStorage.py file, then import it
# import listStorage as listStorage
# import orderStorage as orderStorage

import prodStorage
import orderStorage
import courierStorage as myList

# Create an empty order list of dictionary
curOrderList = []

def orderMenu():
    keepOn = True

    # Setup local variables for order
    # orderNumber = ''
    custName = ''
    custAddress = ''
    custPhone = ''
    STATUS = ''
    action = ''

    while keepOn:
            print("_______________________________")
            print("_ Order Menu                  _")
            print("_                             _")
            print("_ 1)--Print Order Dictionary  _")
            print("_ 2)--Add Order               _")
            print("_ 3)--Update Order            _")
            print("_ 4)--STRETCH update Order    _")
            print("_ 5)--Delete Order            _")
            print("_ 0)--Exit Order menu         _")
            print("_                             _")
            print("_______________________________")
            try:
                choice = input("Please enter your choice :- ")
                if (choice.isdigit()):
                    choice = int(choice)
                    pass
                else:
                    print("Oops, wrong input of \'" + choice + "\' !!!! Enter again please.")
                    continue
                
                if choice in range(0, 6): # Use range(0,6) to control the number of item's choice in menu
                    if (choice == 0):
                        print("Good, you want to exit order menu.")
                        keepOn = False
                    elif (choice == 1):
                        # tempStr = orderFunction.choiceAction(1)
                        print("Print your order details")
                        curOrderList = orderStorage.readOrder()
                        print(f"The order details are listed below :")
                        for orderDetail in curOrderList:
                            print(f"Order[{curOrderList.index(orderDetail)}]\n{orderDetail}")
                        print(f"{curOrderList.index()}")
                    elif (choice == 2):
                        # tempStr = orderFunction.choiceAction(2)
                        print("Enter the order details")
                        # orderNumber = input("Please enter the order number : ")
                        custName = input("Please enter the customer name : ")
                        custAddress = input("Please enter the customer address : ")
                        custPhone = input("Please enter the customer contact phone : ")

                        courierList = myList.openFileToRead()  # Get the updated-currentList 
                        # Print the [index] ---> currentList.item 
                        for courierName in courierList:
                            print(f"[{courierList.index(courierName)}] --> {courierName}")
                        inputIndex = int(input("Enter the index number of the courier that you want to add: "))
                        # Set the status to Preparing for every new order
                        STATUS = 'PREPARING'
                        # orderStorage.writeOrder(orderNumber, custName, custAddress, custPhone, STATUS)
                        orderStorage.writeOrder(custName, custAddress, custPhone, courierList[inputIndex], STATUS)
                    elif (choice == 3):
                        # tempStr = orderFunction.choiceAction(3)
                        action = 'u' # 'u' -> update order
                        curOrderList = orderStorage.updateOrder(action)
                    elif (choice == 4):
                        action = 'su' # 'su' -> STRETCH update order
                        curOrderList = orderStorage.updateOrder(action)  
                    elif (choice == 5):
                        # tempStr = orderFunction.choiceAction(5)
                        action = 'd' # 'd' -> delete order
                        curOrderList = orderStorage.updateOrder(action)
                        # indexNum = input("Which index number wants to be deleted?")
                else:
                    print("Input a wrong selection, try input again!")
                    continue
            except Exception as e:
                print(e)
                continue

# End of orderMenu()