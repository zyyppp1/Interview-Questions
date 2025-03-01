# rBST: Contains
# Implement the r_contains method of the BinarySearchTree class. This method should recursively search the binary search tree for a given value, starting from the root node, and return True if the value is found, and False otherwise.

# You should use a private helper method __r_contains to perform the recursive search. This method should take two arguments: a current node in the tree, and the value to search for.

# The __r_contains method should check whether the current node is None. If it is, the method should return False. If the value to search for is equal to the value of the current node, the method should return True. If the value is less than the value of the current node, the method should call itself recursively with the left child node and the value. If the value is greater than the value of the current node, the method should call itself recursively with the right child node and the value.

# Your implementation of the r_contains method should return the output of the __r_contains method.

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

    def __r_contains(self,currentnode,value):
        if currentnode==None:
            return False
        if currentnode.value==value:
            return True
        if currentnode.value>value:
            return self.__r_contains(currentnode.left,value)
        if currentnode.value<value:
            return self.__r_contains(currentnode.right,value)
        
    def r_contains(self,value):
        return self.__r_contains(self.root,value)
    

        


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('BST Contains 27:')
print(my_tree.r_contains(27))

print('\nBST Contains 17:')
print(my_tree.r_contains(17))
                


"""
    EXPECTED OUTPUT:
    ----------------
    BST Contains 27:
    True

    BST Contains 17:
    False

"""

