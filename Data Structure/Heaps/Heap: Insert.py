# Heap: Insert
# You are provided with a partial implementation of a MaxHeap class.

# The class includes a method for initialization, plus helper methods for getting the left child, the right child, and the parent of a node and swapping elements in the heap.

# Your task is to complete this class by implementing the insert method.

# This method should take an integer as input and add it to the heap. The insertion of a new element should preserve the Max Heap property, i.e., for every node i other than the root, the value of node i is less than or equal to the value of its parent, with the maximum value at the root of the heap.

# Your insert method should be efficient, ideally achieving a time complexity of O(log n), where n is the number of elements in the heap. After inserting the new element at the end of the heap, you should appropriately restructure the heap to maintain the Max Heap property. This typically involves 'bubbling up' the inserted element to its correct position in the heap.

# Remember to handle edge cases, for example when the heap is empty or contains only one or two elements.

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self,value):
        self.heap.append(value)
        current=len(self.heap)-1

        while current>0 and self.heap[current]>self.heap[self._parent(current)]:
            self._swap(current,self._parent(current))   
            current=self._parent(current)

    
myheap = MaxHeap()
myheap.insert(99)
myheap.insert(72)
myheap.insert(61)
myheap.insert(58)

print(myheap.heap)  


myheap.insert(100)

print(myheap.heap)  


myheap.insert(75)

print(myheap.heap)


"""
    EXPECTED OUTPUT:
    ----------------
    [99, 72, 61, 58]
    [100, 99, 61, 58, 72]
    [100, 99, 75, 58, 72, 61]

"""
    