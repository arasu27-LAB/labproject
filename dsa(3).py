class Array:
    flag=0
    def _init_(self,a):
        self.a=[]
    def read(self,n):
        self.a=[0 for i in range(n)]
        for i in range(0,n):
            k=int(input("Enter a number"))
            self.a[i]=k
    def display(self):
        for i in self.a:
            print(i)
    def insert(self,n,p,new):
        for i in range(n-1,p,-1):
            self.a[i]=self.a[i-1]
        self.a[p]=new
    def delete(self,p):
        self.a.pop(p)
    def search(self,key,n):
        for i in range(0,n):
            if(key==self.a[i]):
                print("element",key,"found in position",i)
                Array.flag=1
        if(Array.flag==0):
                print("not found")
n=int(input("Enter the size of array:"))
obj=Array()
obj.read(n)
p=int(input("Enter the index position of the element for insertion:"))
new=int(input("Enter the new element to be inserted:"))
obj.insert(n,p,new)
print("Elements present in the array after insertion:")
obj.display()
d=int(input("Enter the index position of the element to be deleted:"))
if d<n:
    obj.delete(d)
    print("Elements present in the array after insertion:")
    obj.display()
else:
    print("Position does not exist")
key=int(input("Enter key to be search:"))
obj.search(key,n-1)

