# rBST: Insert
# Implement a recursive method called r_insert to insert a value into a binary search tree (BST). The method should maintain the BST property, where the left subtree contains only nodes with values less than the parent node's value, and the right subtree contains only nodes with values greater than the parent node's value. No duplicate values are allowed in the BST.

# The method should have the following signature:



# def r_insert(self, value):


# The method should use a private helper method called __r_insert with the following signature:



# def __r_insert(self, current_node, value):


# The __r_insert method should take the current node and the value to be inserted as arguments. The method should perform the following tasks:



# If the current node is None, create a new node with the given value and return it.

# If the value is less than the current node's value, call the __r_insert method recursively on the left child of the current node.

# If the value is greater than the current node's value, call the __r_insert method recursively on the right child of the current node.

# Return the current node.



# The r_insert method should perform the following tasks:



# If the root of the BST is None, create a new node with the given value and set it as the root.

# Call the __r_insert helper method with the root and the value as arguments.



# The solution should be implemented as a method within the BinarySearchTree class.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    ## WRITE R_INSERT METHODS HERE ##
    def r_insert(self,value):
        if self.root==None:
            self.root=Node(value)
        self.__r_insert(self.root,value)

    def __r_insert(self,node,value):
        if node == None:
            return Node(value)
        if node.value>value:
            node.left=self.__r_insert(node.left,value)
        if node.value<value:
            node.right=self.__r_insert(node.right,value)
        return node


##########################################################   
##   Test code below will print output to "User logs"   ##
##########################################################

def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")

print("\n----- Test: Insert into an empty tree -----\n")
bst = BinarySearchTree()
print("Inserting value:", 5)
bst.r_insert(5)
check(5, bst.root.value, "Root value after inserting 5:")
check(None, bst.root.left, "Left child of root:")
check(None, bst.root.right, "Right child of root:")

print("\n----- Test: Insert values in ascending order -----\n")
bst = BinarySearchTree()
values = [1, 2, 3, 4, 5]
for val in values:
    print("Inserting value:", val)
    bst.r_insert(val)

# Check tree structure
check(1, bst.root.value, "Root value:")
check(2, bst.root.right.value, "Right child of root:")
check(3, bst.root.right.right.value, "Right child of right child of root:")
check(4, bst.root.right.right.right.value, "Right child's right child's right child of root:")
check(5, bst.root.right.right.right.right.value, "Fourth right child of root:")

print("\n----- Test: Insert values in descending order -----\n")
bst = BinarySearchTree()
values = [5, 4, 3, 2, 1]
for val in values:
    print("Inserting value:", val)
    bst.r_insert(val)

# Check tree structure
check(5, bst.root.value, "Root value:")
check(4, bst.root.left.value, "Left child of root:")
check(3, bst.root.left.left.value, "Left child of left child of root:")
check(2, bst.root.left.left.left.value, "Left child's left child's left child of root:")
check(1, bst.root.left.left.left.left.value, "Fourth left child of root:")

print("\n----- Test: Insert values in mixed order -----\n")
bst = BinarySearchTree()
values = [3, 1, 4, 5, 2]
for val in values:
    print("Inserting value:", val)
    bst.r_insert(val)

# Check tree structure
check(3, bst.root.value, "Root value:")
check(1, bst.root.left.value, "Left child of root:")
check(2, bst.root.left.right.value, "Right child of left child of root:")
check(4, bst.root.right.value, "Right child of root:")
check(5, bst.root.right.right.value, "Right child of right child of root:")

print("\n----- Test: Insert duplicate values -----\n")
bst = BinarySearchTree()
values = [3, 3, 3]
for val in values:
    print("Inserting value:", val)
    bst.r_insert(val)

# Check tree structure
check(3, bst.root.value, "Root value:")
check(None, bst.root.left, "Left child of root:")
check(None, bst.root.right, "Right child of root:")
