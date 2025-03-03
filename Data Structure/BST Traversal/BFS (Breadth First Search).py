# BFS (Breadth First Search)
# Write a function called BFS that performs a Breadth-First Search traversal on a binary tree.

# The function should perform the following tasks:

# Initialize the current_node variable with the root of the binary tree.

# Create an empty list called queue to store nodes for processing, and another empty list called results to store the visited nodes in order.

# Append the current_node to the queue.

# Implement a loop that continues until the queue is empty:

# Set current_node to the first element in the queue, and remove this element from the queue.

# Append the value of current_node to the results list.

# If the current_node has a left child, append it to the queue.

# If the current_node has a right child, append it to the queue.

# Return the results list, containing the values of the nodes in the order they were visited during the Breadth-First Search traversal.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
  
    def BFS(self):
        currentnode=self.root
        queue=[]
        result=[]
        queue.append(currentnode)
        while len(queue)>0:
            currentnode=queue.pop(0)
            result.append(currentnode.value)
            if currentnode.left is not None:
                queue.append(currentnode.left)
            if currentnode.right is not None:
                queue.append(currentnode.right)
        return result
                        


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.BFS())



"""
    EXPECTED OUTPUT:
    ----------------
    [47, 21, 76, 18, 27, 52, 82]

 """





                



 