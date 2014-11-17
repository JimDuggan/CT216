# Module: TestQueue.py
from Queue import addElement, removeElement, printList, printArchive
from time import gmtime, strftime, sleep

# This function creates a dictionary element (key-value pairs)
# The second element is a timestamp
def createCustomer(name):
    cust_rec = {
        'name'     : name,
        'time_in'  : strftime("%Y-%m-%d %H:%M:%S", gmtime())
    }
    return cust_rec

# This function adds a new key-value to an existing record
def checkoutCustomer(rec):
    rec['time_out'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    return rec


# Add some test code, create records, add to queue etc.
cr1 = createCustomer("Jane")
print (cr1['name'])
print (cr1['time_in'])
addElement(cr1)

sleep(1.0)

cr2 = createCustomer("John")
print (cr2['name'])
print (cr2['time_in'])
addElement(cr2)

printList()
sleep(1.0)

cr1 = checkoutCustomer(cr1)
removeElement()

sleep(1.0)

cr2 = checkoutCustomer(cr2)
removeElement()

printArchive()




