# You have been provided with a MaxHeap class that includes the _sink_down method.

# ** We will be writing the _sink_down method in the next exercise so please do not peek at it in this exercise.  ;-)

# The class includes a method for initialization, plus helper methods for getting the left child, the right child, and the parent of a node and swapping elements in the heap.

# Your task is to finalize this class by implementing the remove method.

# This method is designed to remove the maximum element from the heap, i.e., the root element, and reorganize the heap so it maintains its max heap property. The max heap property states that for any given node i other than the root, the value of i is at most the value of its parent.

# Here's what your remove method should do in detail:

# If the heap is empty, the remove method should return None.

# If the heap has only one element, the remove method should remove and return this element.

# If the heap has more than one element, the remove method should remove the root of the heap, place the last element in the heap at the root, and then call the _sink_down method to reorganize the heap, maintaining the max heap property.



# Your remove method should be efficient, aiming for a time complexity of O(log n), where n is the number of elements in the heap.

# Remember to consider edge cases where the heap is empty or contains only a few elements.



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
    
    # We will be writing the _sink_down method in the next exercise.
    # But I need to include it here for the tests to work for remove.
    # So, don't peek at this one here.  :-)
    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and 
                    self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            if (right_index < len(self.heap) and 
                    self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
                       
    def remove(self):
        if len(self.heap)==0:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        maxnum=self.heap[0]
        self.heap[0]=self.heap.pop()
        self._sink_down(0)
        return maxnum
    
    
    
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
    