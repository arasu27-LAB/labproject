class Stack:
    def __init__(self):
        self.items = []
    def __repr__(self):
        return repr(self.items) 
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items) 
    def push(self,val):
        self.items.append(val) 
    def pop(self):
        return self.items.pop() 
    def peek(self):
        return self.items[-1]

NumDec=0    
NumBin=''   

NumDec=int(input("Please enter the integer to convert : ")) 
print ("Decimal Number = ",NumDec)
thestack=Stack()    
while NumDec>0 :    
    thestack.push(NumDec%2) 
    NumDec=NumDec//2    
while thestack.isEmpty()==False:    
    NumBin=NumBin+str(thestack.pop())   
print("Binary Number = ",NumBin)
