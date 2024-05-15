class pet:
    
    def __init__(self, name="", type="", age=0):
        self._name = name
        self._type = type
        self._age = age

    
    def setName(self,newname):
        self._name = newname
    
    def setType(self,newtype):
        self._type = newtype
    
    def setAge(self,newage):
        self._age = newage
    
    def getName(self):
        return self._name
    
    def getType(self):
        return self._type
    
    def getAge(self):
        return self._age
   
    
def main():
    pet()
    
    n = input("Enter your pet name: ")
    t = input("Enter your pet type: ")
    a = int(input("Enter your pet age: "))
    
    mypet = pet(n,t,a)
    
    
    
    print(f'Your pet name is: {mypet.getName()}')
    print(f'Your pet type is: {mypet.getType()}')
    print(f'Your pet age is: {mypet.getAge()}')
    


main()