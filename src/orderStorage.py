# This is the mini-project
# File Name     : orderStorage.py
# Date          : 29 Oct 2022
# Developer     : Samuel KO
# Description   : Create a list for app use, a list of methods can be called for file handling
#               : 1) readOrder()                    return myOrderList
#               : 2) openFileToRead()
#               : 3) openFileToUpdate(inItem, updateItem, inAction)
#               : 4) closeFile(fileHandle)
# order_status  : Preparing, Awaiting Pickup, Out-for-Delivery, Delivered

from ctypes.wintypes import SERVICE_STATUS_HANDLE
import os
import csv
from telnetlib import STATUS
import traceback

def readOrder():
    try:    
        # Create an empty Dictionary for reading the orders
        # myOrderList = []
        # list_of_dict = {}

        fileExist = '../data/orderTrans.csv'
        # check if size of file is 0 (i.e. Empty file)
        if (os.stat(fileExist).st_size == 0):
            print('File is empty')
        else:
            # print('File is not empty')

            # With the “With” statement (File Context Manager), you get better syntax and 
            # exceptions handling.  The with statement simplifies exception handling by encapsulating 
            # common preparation and cleanup tasks.  In addition, it will automatically close 
            # the file. With statement provides a way for ensuring that a clean-up is always used.
            # i.e. We didn’t have to write “file.close()”. That will automatically be called.
            # Store the data dictionary into csv format
            
            # with open("../data/orderTrans.csv", 'r') as readFile:
            #     csvReader = csv.reader(readFile)
            #     header = next(csvReader)
            #     count = 0
            #     for readRow in csvReader:
            #         # myOrderDict.append(readRow) # read to list
            #         dict_reader = csv.DictReader(readFile)
            #         list_of_dict.append(dict_reader)
            #         print(list_of_dict)

            with open("../data/orderTrans.csv", 'r') as readCSV:
                csvDictionaryReader = csv.DictReader(readCSV)
                # load into list format  
                myOrderList = list(csvDictionaryReader)
            # print(header)
    except:
        traceback.print_exc()

    return myOrderList
# End of readOrder()


def readCourierList():
    try:    
        fileExist = '../data/orderTrans.csv'
        # check if size of file is 0 (i.e. Empty file)
        if (os.stat(fileExist).st_size == 0):
            print('File is empty')
        else:
            with open("../data/orderTrans.csv", 'r') as readCSV:
                csvDictionaryReader = csv.DictReader(readCSV)
                # load into list format  
                myOrderList = list(csvDictionaryReader)
            # print(header)
    except:
        traceback.print_exc()

    return myOrderList
# End of readCourierList()

# def writeOrder(inNumber, inName, inAddress, inPhone, inSTATUS):
def writeOrder(inName, inAddress, inPhone, inCourierName, inSTATUS):
    # Writing order to CSV files using the DictWriter class.  If each row of the CSV file is a dictionary, 
    # Use the DictWriter class of the csv module to write the dictionary to the orderTrans.csv file
    # under '../data/' directory

    # define a dictionary with key value pairs

    # myOrderList = [{'customer_name':'Nishu','customer_address':'address in Manchester','customer_phone':'601','status':'processing'},
    #                 {'customer_name':'Megha','customer_address':'address 1 for Megha','customer_phone':'602','status':'processing'},
    #                 {'customer_name':'Zach', 'customer_address':'.address near the city center','customer_phone':'603','status':'processing'},
    #                 {'customer_name':'Rachel','customer_address':'Bolton of UK','customer_phone':'604','status':'processing'},
    #                 {'customer_name':'Rachal','customer_address':'The main office of Generation','customer_phone':'605','status':'processing'},
    #                 {'customer_name':'Tom','customer_address':'Not specified','customer_phone':'606','status':'processing'}]

    myOrderList = {}

    # below field must match with the keys in myOrderList
    # fields = ['order_number','customer_name','customer_address','customer_phone','status']
    fields = ['customer_name','customer_address','customer_phone','couriers','status']

    orderFile = "../data/orderTrans.csv"

    # Format of myOrderList is listed as below:
    # myOrderList = [{'customer_name':'John','customer_address':'address in the north of Manchester','customer_phone':'609','status':'Out-for-Delivery'}]

    # Prepare inserting keys and values to the dictionary
    # myOrderList = [{'order_number':inNumber, 'customer_name':inName, 'customer_address':inAddress, 'customer_phone':inPhone, 'status':inSTATUS}]
    myOrderList = [{'customer_name':inName, 'customer_address':inAddress, 'customer_phone':inPhone, 'couriers':inCourierName,'status':inSTATUS}]
    
    # With the “With” statement (File Context Manager), you get better syntax and 
    # exceptions handling.  The with statement simplifies exception handling by encapsulating 
    # common preparation and cleanup tasks.  In addition, it will automatically close 
    # the file. With statement provides a way for ensuring that a clean-up is always used.
    # i.e. We didn’t have to write “file.close()”. That will automatically be called.
    with open(orderFile, 'a+') as csvFile:
        # --------------------Original code for reference-------------------------
        # with open(orderFile, 'a+') as csvFile:
        #     writer = csv.DictWriter(csvFile, fieldnames=fields)
        #     writer.writeheader()
        #     writer.writerows(myOrderList)
        # --------------------End of code referencing____-------------------------
        writer = csv.DictWriter(csvFile, fieldnames=fields)
        # check if size of file is 0 (i.e. Empty file)
        if (os.stat(orderFile).st_size == 0):
            print('File is empty, write the csv file header now')
            writer.writeheader()
            print("SET statu to -> \'" + inSTATUS + "\'")
        
        writer.writerows(myOrderList)
        print(f"Added the order :\n{myOrderList}")

# End of writeOrder()

# Description :
#              inAction  : 'u' -> update
#                        : 'd' -> delete
#              order_status = 1) Preparing 2) Awaiting Pickup 3) Out-for-Delivery 4) Delivered

def updateOrder(inAction):
    # below field must match with the keys in myOrderList
    # fields = ['order_number','customer_name','customer_address','customer_phone','status']
    fields = ['customer_name','customer_address','customer_phone','couriers','status']

    try:
        currentOrderList = readOrder()
        count = 0
        print("The orders are listed as below :")
        for itemList in currentOrderList:
            print(f"Index[{count}]--->{itemList}")
            count += 1
        # Finished print out the list

        # Get index for delete
        orderIndex = int(input("Enter the index that want to process : "))
        if (inAction == 'd'): # handle for delete order
            currentOrderList.pop(orderIndex)
            print(f"Record with index[{orderIndex}] to delete")    
        elif(inAction == 'u'): # handle for update order
            inStatus = 'status'
            print(f"Record with index[{orderIndex}] to update")    
            print("Please select status to update : ")
            print("   1) Preparing ")
            print("   2) Awaiting Pickup ")
            print("   3) Out-for-Delivery ")
            print("   4) Delivered")
            selection = int(input("Enter your choice : "))
            if (selection == 1):
                selectSTATUS = "PREPARING"
            elif(selection == 2):
                selectSTATUS = "AWAITING PICKUP"
            elif(selection == 3):
                selectSTATUS = "OUT-FOR-DELIVERY"
            elif(selection == 4):
                selectSTATUS = "DELIVERED"
            currentOrderList[orderIndex][inStatus] = selectSTATUS  # Update the desired status 
        elif(inAction == 'su'): # handle for STRETCH update order
            inStatus = 'status'
            localCount = 0
            for key, item in itemList.items():  # Iterate through the selected dictionary
                print(f'[{localCount}]-->{key}:{item}')  # Create a dynamic menu for selection
                localCount += 1
            getPropertyIndex = input("Enter the property index to update the specific preperty : ")
            if (getPropertyIndex == ''):
                print("Update Aborted")
            else: # the input index match!!!      (getPropertyIndex == itemList[key]):
                # Debug statement : print("Input index -> " + getPropertyIndex)
                # Reset localCount to zero
                localCount = 0
                for key, item in itemList.items():  # Iterate through the selected dictionary
                    ## Debug statement : print(f'[{localCount}]-->{key}:{item}')
                    if (localCount == int(getPropertyIndex)):
                        # Debug statement : print(f'Inside if loop : [{localCount}]-->{key}:{item}')  # Create a dynamic menu for selection
                        newPropertyValue = input(f"Please enter the new value for {key} to be updated :")
                        # update the property 'currentOrderList[orderIndex][key]' for user input value
                        currentOrderList[orderIndex][key] = newPropertyValue
                        break
                    else: 
                        localCount += 1 # get next property
        # Write/Update back the results to csv file
        orderFile = "../data/orderTrans.csv"
        with open(orderFile, 'w') as csvFile:
             writer = csv.DictWriter(csvFile, fieldnames=fields)
             # check if size of file is 0 (i.e. Empty file)
             if (os.stat(orderFile).st_size == 0):
                writer.writeheader()
                # print("SET statu to -> \'" + inSTATUS + "\'")
        
             writer.writerows(currentOrderList)
             if (inAction == 'd'):
                print(f"Order Index[{orderIndex}] has been deleted")
             else:
                print(f"Order Index[{orderIndex}] has been updated")

    except:
        traceback.print_exc()

    return currentOrderList
# End of updateOrder()
