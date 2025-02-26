
# MinHeap: Insert
# You are provided with a partial implementation of a MinHeap class.

# The class includes a method for initialization, plus helper methods for getting the left child, the right child, and the parent of a node and swapping elements in the heap.

# Your task is to complete this class by implementing the insert method.

# This method should take an integer as input and add it to the heap. The insertion of a new element should preserve the Min Heap property, i.e., for every node i other than the root, the value of node i is greater than or equal to the value of its parent, with the minimum value at the root of the heap.

# Your insert method should be efficient, ideally achieving a time complexity of O(log n), where n is the number of elements in the heap. After inserting the new element at the end of the heap, you should appropriately restructure the heap to maintain the Min Heap property. This typically involves 'bubbling up' the inserted element to its correct position in the heap.

# Remember to handle edge cases, for example when the heap is empty or contains only one or two elements.

class MinHeap:
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

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
 
        while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
    
 
myheap = MinHeap()
myheap.insert(12)
myheap.insert(10)
myheap.insert(8)
myheap.insert(6)

print(myheap.heap)  # [6, 8, 10, 12]

myheap.insert(4)

print(myheap.heap)  # [4, 6, 10, 12, 8]

myheap.insert(2)

print(myheap.heap)  # [2, 6, 4, 12, 8, 10]


"""
    EXPECTED OUTPUT:
    ----------------
    [6, 8, 10, 12]
    [4, 6, 10, 12, 8]
    [2, 6, 4, 12, 8, 10]

"""
