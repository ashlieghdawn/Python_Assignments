class Protected:
    def __init__(self):
        self._protectedVar = 0
        self.__privateVar = 16

    def getPrivate(self):
        print(self.__privateVar)

    
        
obj = Protected()
obj._protectedVar = 24
print(obj._protectedVar)
obj.getPrivate()


