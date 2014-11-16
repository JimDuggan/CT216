# define a function...
def HelloWorld(msg):
    print("Calling function...")
    print(msg)
    return 'Success'

# useful code at the end of each module.
if __name__ == '__main__':
    print 'This program is being run by itself'
    status = HelloWorld('Hello World, Welcome to CT216 Project')
    print status
else:
    print 'I am being imported from another module'


