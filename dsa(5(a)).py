class Stack:
   def __init__(self):
       self.stack = []

   def add(self, dataval):
       self.stack.append(dataval)
               
   def remove(self):
       if len(self.stack) <= 0:
           return ("No element in the Stack")
       else:
           return self.stack.pop()

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.add("Wed")
AStack.add("Thu")
print("Elements in Stack:",AStack.stack)
print("Popped element is:",AStack.remove())
print("Popped element is:",AStack.remove())

