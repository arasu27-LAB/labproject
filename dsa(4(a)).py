class Node:  
    def __init__(self,data):  
        self.data = data  
        self.next = None
class SinglyLinkedList:  
    def __init__(self):  
        self.head = None  
        self.tail = None  
          
    def addNode(self, data):  
        newNode = Node(data)  
        if(self.head == None):  
            self.head = newNode  
            self.tail = newNode  
        else:  
            self.tail.next = newNode  
            self.tail = newNode
    def atbegin(self,data):
        if(self.head == None):  
            self.head = newNode  
            self.tail = newNode  
        else:  
            newNode=Node(data)
            newNode.next=self.head
            self.head=newNode
    def atend(self,data):
        if(self.head == None):  
            self.head = newNode  
            self.tail = newNode
            return
        else:  
            newNode=Node(data)
            last=self.head
            while(last.next):
                last=last.next
            last.next=newNode
    def removenode(self,key):
        headVal=self.head
        if(headVal is not None):
            if(headVal.data==key):
                self.head=headVal.next
                headVal=None
                return
        while (headVal is not None):
            if headVal.data == key:
                break
            prev = headVal
            headVal = headVal.next
        if (headVal == None):
            return
        prev.next = headVal.next
        headVal = None
    def display(self):   
        current = self.head
        if(self.head == None):  
            print("List is empty")  
            return
        print("\nNodes of singly linked list: ")
        while(current != None):   
            print(current.data),
            current = current.next;
sList = SinglyLinkedList()
sList.addNode(2)
sList.addNode(3)  
sList.addNode(4)  
sList.addNode(5)  
sList.display()
sList.atbegin(1)
sList.display()
sList.atend(6)
sList.display()
sList.removenode(5)
sList.display()
