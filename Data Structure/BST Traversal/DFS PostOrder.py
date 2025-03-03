# DFS PostOrder
# Write a function called dfs_post_order that performs a Depth-First Search (DFS) traversal on a binary tree using the Post-Order approach.

# The function should perform the following tasks:

# Create an empty list called results to store the visited nodes in order.

# Define a nested function called traverse that takes a current_node as an argument.

# In the traverse function, perform the following tasks:

# If the current_node has a left child, recursively call the traverse function with the left child as an argument.

# If the current_node has a right child, recursively call the traverse function with the right child as an argument.

# Append the value of the current_node to the results list.

# Call the traverse function with the root of the binary tree as the initial argument.

# Return the results list, containing the values of the nodes in the order they were visited during the Post-Order Depth-First Search traversal.


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
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    
    def dfs_pre_order(self):
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results

    def dfs_post_order(self):
        result=[]
        currentnode=self.root
        def traverse(node):
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
            result.append(node.value)

        traverse(currentnode)
        return result




my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.dfs_post_order())



"""
    EXPECTED OUTPUT:
    ----------------
    [18, 27, 21, 52, 82, 76, 47]

 """
