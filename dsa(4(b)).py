class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doubly_linked_list:
    def __init__(self):
        self.head = None

    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

    def append(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return
    def remove(self):
        if self.head is None:
            return
        else:
            last = self.head
            while (last.next.next is not None):
                last = last.next
            last.next = None
            return
        
    def listprint(self, node):
        print("The nodes presented in doubly linked list are:")
        while (node is not None):
            print(node.data),
            last = node
            node = node.next

Dllist = doubly_linked_list()
Dllist.push(12)
Dllist.append(9)
Dllist.push(8)
Dllist.push(62)
Dllist.append(45)
Dllist.listprint(Dllist.head)
print("\nAfter removing last element:")
Dllist.remove()
Dllist.listprint(Dllist.head)


