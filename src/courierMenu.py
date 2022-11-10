# This is the mini-project
# File Name     : courierMenu.py
# Date          : 04 Nov 2022
# Developer     : Samuel KO
# Description   : Build a Courier Menu for
#               : 1) Courier menu
#               : 2) Add courier menu
#               : 3) Update courier menu
#               : 4) Delete courier menu
#               : 0) Return to Main Menu

# Set the global myCourierList as global variable by 
# putting it to listStorage.py file, then import it
import courierStorage as myList

def courierMenu():
    KeepOn = True

    # Create an empty courier list
    currentList = []

    while KeepOn:
            print("___________________________")
            print("_ Courier Menu            _")
            print("_                         _")
            print("_ 1)--Retrieve Courier    _")
            print("_ 2)--Add New Courier     _")
            print("_ 3)--Update Courier      _")
            print("_ 4)--Delete Courier      _")
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
                        print("Good, you want to exit courier menu.")
                        KeepOn = False
                    elif (choice == 1):
                         currentList = myList.openFileToRead()
                         print(currentList)
                    elif (choice == 2):
                        # Add courier to the current courier list
                        inputItem = input("Enter courier : ")
                        if inputItem not in currentList:
                            myList.openFileToWrite(inputItem)
                            currentList.append(inputItem)
                        print("List after input the item : ", currentList)
                    elif (choice == 3):
                        currentList = myList.openFileToRead()  # Get the updated-currentList 
                        # Print the [index] ---> currentList.item 
                        for courierName in currentList:
                            print(f"[{currentList.index(courierName)}] --> {courierName}")
                        inputIndex = int(input("Enter the index number of the courier that you want to update: "))
                        itemToUpdate = input("What you want to update: ")
                        
                        print(f"Wanted to update from {currentList[inputIndex]} to {itemToUpdate}")
                        inputItem = currentList[inputIndex]
                        if (len(currentList) != 0):
                            if inputItem in currentList:
                                myList.openFileToUpdate(inputItem, itemToUpdate, 'u')
                                currentList[currentList.index(inputItem)] = itemToUpdate
                                print(f"{inputItem} is updated to {itemToUpdate} from courier list")
                        else:
                            print(f"Updated! the courier {inputItem} has been updated to {itemToUpdate}!")
                            continue

                    elif (choice == 4):
                        currentList = myList.openFileToRead()  # Get the updated-currentList 
                        # Print the [index] ---> currentList.item 
                        for courierName in currentList:
                            print(f"[{currentList.index(courierName)}] --> {courierName}")
                        wantToRemoveItemIndex = int(input("Enter the courier that you want to delete: "))
                        wantToRemoveItem = currentList[wantToRemoveItemIndex]
                        print("Wanted to delete courier", wantToRemoveItem.strip())
                        if (len(currentList) != 0):
                            if wantToRemoveItem in currentList:
                                myList.openFileToUpdate(wantToRemoveItem, '', 'd')
                                currentList.remove(wantToRemoveItem)
                                print(f"{wantToRemoveItem} is removed from courier list")
                        else:
                            print("The courier list is empty, nothing to be deleted!")
                            continue
                    else:
                        print(f"{choice} is not a valid menu selection in here, please try again!")
                        continue
            except Exception as e:
                    print(e)    
                    continue
