class Queue:
   def __init__(self):
      self.queue = list()

   def addtoq(self,dataval):
       if dataval not in self.queue:
           self.queue.insert(0,dataval)
           return True
       return False
# Pop method to remove element
   def remove(self):
       if len(self.queue)>0:
           return self.queue.pop()
       return ("No elements in Queue!")

Q = Queue()
Q.addtoq("Mon")
Q.addtoq("Tue")
Q.addtoq("Wed")
Q.addtoq("Thu")
print("Elements in Queue:",Q.queue)
print("Removed Element from Queue:",Q.remove())
print("Removed Element from Queue:",Q.remove())
