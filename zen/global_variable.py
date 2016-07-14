#how to use global variables, how to set
myGlobal = 5

def set_global():
    myGlobal = 42

def print_global():
    print myGlobal

#this will print 5, instead of 42
set_global()
print_global()

#you have to put "global" before a global variable so python can find it
def set_global_2():
    global myGlobal
    myGlobal = 42

#this will print 42
set_global_2()
print_global()

#more info...
#http://stackoverflow.com/questions/423379/using-global-variables-in-a-function-other-than-the-one-that-created-them
