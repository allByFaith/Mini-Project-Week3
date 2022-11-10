# This is the mini-project
# File Name     : courierStorage.py
# Date          : 04 Nov 2022
# Developer     : Samuel KO
# Description   : Create a list for app use, a list of methods can be called for file handling
#               : 1) openFileToWrite(inItem)
#               : 2) openFileToRead()
#               : 3) openFileToUpdate(inItem, updateItem, inAction)
#               : 4) closeFile(fileHandle)
#
# e.g. myList = ["Coca Cola Classic","Coke Zero","Pepsi Cola","Diet Pepsi","Sprite","Fanta","Dr. Peper"]
import traceback

# openFileToRead() for reading a file
def openFileToWrite(inItem):
    try:
        # traceback.print_exc()
        fileHandle = open("../data/courier.txt", "a+")
        inItem = inItem + "\n"
        fileHandle.write(inItem)
    except:
        traceback.print_exc()
    
    closeFile(fileHandle)
# End of openFileToWrite()

# openFileToWrite() for writing a file
def openFileToRead():
    # Create a temperary list for use
    tempList = []
    try:
        fileHandle = open("../data/courier.txt", "r")  # Open courier.txt which under data/ directory for reading 
        print("Open file to read the courier list :-")
        tempFileObj = fileHandle.readlines()
        for readItem in tempFileObj:
            if('\n' in readItem):
                readItem = readItem[:-1]
            tempList.append(readItem)
    except:
        fileHandle = open("../data/courier.txt", "x")
        print("Create file")

    closeFile(fileHandle)
    return tempList
# End of openFileToRead()

def openFileToUpdate(inItem, updatedItem, inAction):
    import os

    # use two value for inAction : 1) u - update item
    #                            : 2) d - delete item

    fileHandle = open("../data/temp.txt", "x")
    try:
        with open("../data/courier.txt", "r") as inputW:
            with (open("../data/temp.txt", "a")) as outputW:
                for readItem in inputW:
                    if((readItem.strip() != inItem)):
                       outputW.write(readItem)
                    else:
                        if(inAction == 'd'):
                            pass
                        elif(inAction == 'u'):
                            outputW.write(updatedItem + "\n")

        os.replace('../data/temp.txt', '../data/courier.txt')                
    except:
        traceback.print_exc()
    
    closeFile(fileHandle)
# End of openFileToUpdate()


def closeFile(inFileHandle):
    inFileHandle.close()

# Below code use for self testing....
# def main():
#     f = openFileToRead()
#     # print(f)
#     # item = "New Item"
#     # f = openFileToWrite(item)
    
#     finalStatus = closeFile(f)

# main()
