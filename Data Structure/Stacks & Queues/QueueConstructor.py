class Node():
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue():
    def __init__(self,value):
        newNode=Node(value)
        self.first=newNode
        self.last=newNode
        self.length=1

    def printQueue(self):
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next
            



my_queue = Queue(4)

print('First:', my_queue.first.value)
print('Last:', my_queue.last.value)
print('Length:', my_queue.length)


"""
    EXPECTED OUTPUT:
    ----------------
    First: 4
    Last: 4
    Length: 1

"""