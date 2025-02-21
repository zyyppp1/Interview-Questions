class Node():
    def __init__(self,value):
        self.value=value
        self.prev=None
        self.next=None
        
class DoublyLinkedList():
    def __init__(self,value):
        newNode=Node(value)
        self.head=newNode
        self.tail=newNode
        self.length=1

    def printlist(self):
        temp=self.head
        if temp is not None:
            for _ in range(self.length):
                print(temp.value)
                temp=temp.next




my_doubly_linked_list = DoublyLinkedList(7)

print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length)



"""
    EXPECTED OUTPUT:
    ----------------
    Head: 7
    Tail: 7
    Length: 1

"""
