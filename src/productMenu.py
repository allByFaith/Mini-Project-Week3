# This is the mini-project
# File Name     : miniProjectWeek1.py
# Date          : 21 Oct 2022
# Developer     : Samuel KO
# Description   : Build a Product Menu for
#               : 1) Product menu
#               : 2) Add Product menu
#               : 3) Update product menu
#               : 4) Delete product menu
#               : 0) Return to Main Menu

# Set the global myProdList as global variable by 
# putting it to listStorage.py file, then import it
import prodStorage as myList

def productMenu():
    KeepOn = True

    # Create an empty Product list
    currentList = []

    while KeepOn:
            print("___________________________")
            print("_ Product Menu            _")
            print("_                         _")
            print("_ 1)--Retrieve Product    _")
            print("_ 2)--Add New Product     _")
            print("_ 3)--Update Product      _")
            print("_ 4)--Delete Product      _")
            print("_ 0)--Return to Main Menu _")
            print("_                         _")
            print("___________________________")

            try:
                choice = input("Please enter your choice :- ")
                if (choice.isdigit()):
                    choice = int(choice)
                    pass
                else:
                    print("Oops, wrong input of \'" + choice + "\' !!!! Enter again please.")
                    continue
                
                if choice in range(0, 5):
                    if (choice == 0):
                        print("Good, you want to exit product menu.")
                        KeepOn = False
                    elif (choice == 1):
                         currentList = myList.openFileToRead()
                         print(currentList)
                    elif (choice == 2):
                        inputItem = input("Enter product : ")
                        if inputItem not in currentList:
                            myList.openFileToWrite(inputItem)
                            currentList.append(inputItem)
                        print("List after input the item : ", currentList)
                    elif (choice == 3):
                        # inputItem = input("Enter the name of product that you want to update: ")
                        # itemToUpdate = input("What you want to update: ")
                        # currentList[currentList.index(inputItem)] = itemToUpdate
                        # print(f"Updated! the product {inputItem} has been updated to {itemToUpdate}!")
                    
                        inputItem = input("Enter the name of product that you want to update: ")
                        itemToUpdate = input("What you want to update: ")
                        print(f"Wanted to update from {inputItem} to {itemToUpdate}")
                        currentList = myList.openFileToRead()  # Get the updated-currentList 
                        if (len(currentList) != 0):
                            if inputItem in currentList:
                                myList.openFileToUpdate(inputItem, itemToUpdate, 'u')
                                currentList[currentList.index(inputItem)] = itemToUpdate
                        else:
                            print(f"Updated! the product {inputItem} has been updated to {itemToUpdate}!")
                            continue

                    elif (choice == 4):
                        wantToRemoveItem = input("Enter the product that you want to delete: ")
                        print("Wanted to delete item", wantToRemoveItem)
                        currentList = myList.openFileToRead()  # Get the updated-currentList 
                        if (len(currentList) != 0):
                            if wantToRemoveItem in currentList:
                                myList.openFileToUpdate(wantToRemoveItem, '', 'd')
                                currentList.remove(wantToRemoveItem)
                        else:
                            print("The product list is empty, nothing to be deleted!")
                            continue
                    else:
                        print(f"{choice} is not a valid menu selection in here, please try again!")
                        continue
            except Exception as e:
                    print(e)    
                    continue
