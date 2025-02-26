# Implement the _sink_down helper method in the MaxHeap class. This method is a private helper method that is crucial to maintaining the max heap property when the root element is removed from the heap.

# The class includes a method for initialization, plus helper methods for getting the left child, the right child, and the parent of a node and swapping elements in the heap.

# Here's what your _sink_down method needs to do in detail:

# The method takes an index as a parameter. This index is the position of the node in the heap that needs to be 'sunk down' to its appropriate position to maintain the max heap property.

# In each iteration of its main loop, the method identifies the maximum of the node at the provided index, its left child, and its right child. The indexes of the left and right children can be determined using the _left_child and _right_child methods, respectively.

# If the maximum value is found to be at the provided index, the method ends. Otherwise, the node at the provided index is swapped with the node with the maximum value. The _swap method can be used for this.

# The index of the node with the maximum value is then set as the provided index for the next iteration of the loop.



# The _sink_down method should aim for an efficient time complexity of O(log n), where n is the number of elements in the heap.

# Consider various edge cases, such as when the node to sink down is already at its correct position, or when it needs to be sunk down multiple levels in the heap.



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

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    # WRITE THE _SINK_DOWN METHOD HERE #
    #                                  #
    #                                  #
    #                                  #
    #                                  #
    ####################################
                       
    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value
        
        

myheap = MaxHeap()
myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)

print(myheap.heap)


myheap.remove()

print(myheap.heap)


myheap.remove()

print(myheap.heap)


"""
    EXPECTED OUTPUT:
    ----------------
    [95, 75, 80, 55, 60, 50, 65]
    [80, 75, 65, 55, 60, 50]
    [75, 60, 65, 55, 50]

"""
