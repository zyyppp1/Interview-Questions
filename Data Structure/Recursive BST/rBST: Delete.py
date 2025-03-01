# rBST: Delete
# Write two Python functions for the BinarySearchTree class: delete_node and __delete_node.

# These functions should work together to delete a node with a given integer value from the binary search tree while maintaining its structure and ordering after deletion.

# delete_node(value): This function should take an integer value as input and call the __delete_node function with the root node of the binary search tree and the input value. It should then update the root of the binary search tree with the returned value from the __delete_node function.

# __delete_node(current_node, value): This function should take a Node object (current_node) and an integer value as input. It should be a recursive helper function that facilitates the node deletion process for the delete_node function. The function should have the following behavior:

# If the current_node is None, return None.

# If the input value is smaller than the value of the current_node, set the left child of the current_node to the result of calling __delete_node with the left child of the current_node and the input value.

# If the input value is larger than the value of the current_node, set the right child of the current_node to the result of calling __delete_node with the right child of the current_node and the input value.

# If the input value is equal to the value of the current_node, perform the deletion according to the following cases:

# If the current_node has no children, return None.

# If the current_node has only a left child, return the left child.

# If the current_node has only a right child, return the right child.

# If the current_node has both left and right children, find the minimum value in the right subtree of the current_node, replace the value of the current_node with the found minimum value, and then delete the node with the minimum value in the right subtree using a recursive call to __delete_node.

# Return the current_node after making the necessary updates.

# Your implementation should ensure that the binary search tree maintains its structure and ordering after the deletion operation.



# Please click on "Hints" (above) to see the pseudo-code.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

          
    def __r_insert(self, current_node, value):
        if current_node == None: 
            return Node(value)   
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value) 
        return current_node    

    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        self.__r_insert(self.root, value)  


    def min_value(self, current_node):
        while (current_node.left is not None):
            current_node = current_node.left
        return current_node.value 

    def delete_node(self,value):
        self.__delete_node(self.root,value)

    def __delete_node(self,node,value):
        if node==None:
            return None
        if node.value>value:
            node.left=self.__delete_node(node.left,value)
        if node.value<value:
            node.right=self.__delete_node(node.right,value)
        else:
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            else:
                subtreemin=self.min_value(node.right)
                node.value=subtreemin
                self.__delete_node(node.right,subtreemin)
                return node

##########################################################   
##   Test code below will print output to "User logs"   ##
##########################################################

def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")


# test_delete_node_no_children
print("\n----- Test: Delete node with no children -----\n")
bst = BinarySearchTree()
values = [5, 3, 8]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(3)
check(None, bst.root.left, "Left child of root after deleting 3:")


# test_delete_node_only_left_child
print("\n----- Test: Delete node with only left child -----\n")
bst = BinarySearchTree()
values = [5, 3, 8, 1]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(3)
check(1, bst.root.left.value, "Left child of root after deleting 3:")


# test_delete_node_only_right_child
print("\n----- Test: Delete node with only right child -----\n")
bst = BinarySearchTree()
values = [5, 3, 8, 9]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(8)
check(9, bst.root.right.value, "Right child of root after deleting 8:")


# test_delete_node_two_children
print("\n----- Test: Delete node with two children -----\n")
bst = BinarySearchTree()
values = [5, 3, 8, 1, 4, 7, 9]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(3)
check(4, bst.root.left.value, "Left child of root after deleting 3:")


# test_delete_root
print("\n----- Test: Delete root -----\n")
bst = BinarySearchTree()
values = [5, 3, 8]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(5)
check(8, bst.root.value, "Root value after deleting 5:")


# test_delete_non_existent_node
print("\n----- Test: Attempt to delete a non-existent node -----\n")
bst = BinarySearchTree()
values = [5, 3, 8]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
original_root_value = bst.root.value
bst.delete_node(10)
check(original_root_value, bst.root.value, "Root value after attempting to delete 10:")
