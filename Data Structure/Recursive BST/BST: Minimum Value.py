# BST: Minimum Value
# Implement a method called min_value that finds and returns the minimum value in a binary search tree (BST) starting from a given node.

# The method should take one argument, current_node, which is the node from where the search for the minimum value begins. The method should follow these steps:



# Traverse the left subtree of the BST from the current_node, moving to the left child of each node until there is no left child available.

# Once the leftmost node is found, return its value as the minimum value in the BST starting from the given node.



# The solution should be implemented as a method within the BinarySearchTree class.

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
    
    def min_value(self,node):
        while node.left is not None:
            node=node.left
        else:
            return node.value

        

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)


print( my_tree.min_value(my_tree.root) )

print( my_tree.min_value(my_tree.root.right) )
            

"""
    EXPECTED OUTPUT:
    ----------------
	18
	52

"""

