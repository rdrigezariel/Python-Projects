class EncapsulationAssignment:
    # initialize the protected and private variable
    def __init__(self):
        self._protectedVar = 1
        self.__privateVar = 2

    # method to get value of private variable
    def getPrivateVar(self):
        print(self.__privateVar)
    # method to set value of private variable
    def setPrivateVar(self, private):
        self.__privateVar = private

obj = EncapsulationAssignment()

# print screen protected variable
print (obj._protectedVar)

# set and print screen private variable
obj.getPrivateVar()
obj.setPrivateVar(7)
obj.getPrivateVar()
