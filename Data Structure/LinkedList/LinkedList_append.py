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
    
myLinkedlist=Linkedlist(10)
myLinkedlist.printlist()

myLinkedlist.append(1)
myLinkedlist.printlist()

myLinkedlist.append(2)
myLinkedlist.printlist()

myLinkedlist.append(3)
myLinkedlist.printlist()
