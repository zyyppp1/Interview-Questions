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

    def prepend(self,value):
        NewNode=Node(value)
        if self.length ==0:
            self.head=NewNode
            self.tail=NewNode
        else:
            NewNode.next=self.head
            self.head=NewNode
        self.length+=1
        return True

    def popfirst(self):
        if self.length ==0:
            return None
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp
    
    def Get(self,index):
        if index < 0 or index > self.length:
            return False
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp.value
    
    def Set(self,index,value):
        if index < 0 or index > self.length:
            return False
        temp=self.head
        for _ in range(index):
            temp=temp.next
        temp.value=value
        return True

mylinklist=Linkedlist(0)
mylinklist.append(1)
mylinklist.append(2)
mylinklist.append(3)
print(mylinklist.Get(1))
mylinklist.Set(1,5)
print(mylinklist.Get(1))
