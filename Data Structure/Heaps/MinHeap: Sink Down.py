# Implement the _sink_down helper method in the MinHeap class. This method is a private helper method that is crucial to maintaining the min heap property when the root element is removed from the heap.

# The class includes a method for initialization, plus helper methods for getting the left child, the right child, and the parent of a node and swapping elements in the heap.

# Here's what your _sink_down method needs to do in detail:

# The method takes an index as a parameter. This index is the position of the node in the heap that needs to be 'sunk down' to its appropriate position to maintain the min heap property.

# In each iteration of its main loop, the method identifies the minimum of the node at the provided index, its left child, and its right child. The indexes of the left and right children can be determined using the _left_child and _right_child methods, respectively.

# If the minimum value is found to be at the provided index, the method ends. Otherwise, the node at the provided index is swapped with the node with the minimum value. The _swap method can be used for this.

# The index of the node with the minimum value is then set as the provided index for the next iteration of the loop.



# The _sink_down method should aim for an efficient time complexity of O(log n), where n is the number of elements in the heap.

# Consider various edge cases, such as when the node to sink down is already at its correct position, or when it needs to be sunk down multiple levels in the heap.

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

    # def _sink_down(self, index):
    #     min_index = index
    #     while True:
    #         left_index = self._left_child(index)
    #         right_index = self._right_child(index)

    #         if (left_index < len(self.heap) and 
    #                 self.heap[left_index] < self.heap[min_index]):
    #             min_index = left_index

    #         if (right_index < len(self.heap) and 
    #                 self.heap[right_index] < self.heap[min_index]):
    #             min_index = right_index

    #         if min_index != index:
    #             self._swap(index, min_index)
    #             index = min_index
    #         else:
    #             return

    def _sink_down(self,index):
        minindex=index

        while True:
            leftindex=self._left_child(index)
            rightindex=self._right_child(index)

            if leftindex<len(self.heap) and self.heap[leftindex]<self.heap[minindex]  :
                minindex=leftindex
            if  rightindex<len(self.heap) and self.heap[rightindex]<self.heap[minindex] :
                minindex=rightindex
            if minindex!=index:
                self._swap(index,minindex)
                index=minindex
            else:
                return 

    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return min_value
        
        
        
myheap = MinHeap()
myheap.insert(12)
myheap.insert(10)
myheap.insert(8)
myheap.insert(6)
myheap.insert(4)
myheap.insert(2)

print(myheap.heap)  # [2, 6, 4, 12, 8, 10]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 2, Heap: [4, 6, 10, 12, 8]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 4, Heap: [6, 8, 10, 12]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 6, Heap: [8, 12, 10]



"""
    EXPECTED OUTPUT:
    ----------------
    [2, 6, 4, 12, 8, 10]
    Removed: 2, Heap: [4, 6, 10, 12, 8]
    Removed: 4, Heap: [6, 8, 10, 12]
    Removed: 6, Heap: [8, 12, 10]

"""