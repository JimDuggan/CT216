# Module: Queue.py

# Useful List methods
#   list.append(x)
#   list.insert(i,x)  insert item at a given position
#   list.remove(x)    remove x from list
#   list.pop([i])     remove item at position of list, default removes last item
#   list.index(x)     return index of item x (first occurrence)
#   list.count(x)     counts the number of times x appears on the list

theQueue   = [] # Global data for this module, can be changed by functions
theArchive = [] # Global data for this module, can be changed by functions

# Queue order is FIFO (First in First Out)

def addElement(e):
    theQueue.insert(0,e)

def removeElement():
    e = theQueue.pop()
    archive(e)
    return e

def printList():
    print("Printing the queue:")
    for x in theQueue:
        print (x)

def archive(e):
    theArchive.append(e)


def printArchive():
    print("Printing the archive:")
    for x in theArchive:
        print (x)

# useful code at the end of each module.
if __name__ == '__main__':
    print 'This program is being run by itself'
else:
    print 'I am being imported from another module'




