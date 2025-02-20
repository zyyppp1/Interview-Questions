class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
class Linkedlist:
    def __init__(self,value):
        newNode=Node(value)
        self.head=newNode
        self.tail=newNode
        self.length=1

    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next 

    def append(self,value):
        newNode=Node(value)
        if self.head is None:
             self.head=newNode
             self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
        self.length+=1
        return True
    
    def pop(self):
        if self.length ==0:
            return None
        pre=self.head
        temp=self.head
        while temp.next is not None:
            pre=temp
            temp=temp.next
        self.tail=pre
        pre.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp
    

    
mylinklist=Linkedlist(1)

mylinklist.append(2)

mylinklist.printlist()
#2 items in 
print(mylinklist.pop())
#1 item in
print(mylinklist.pop())
#0 item
print(mylinklist.pop())
