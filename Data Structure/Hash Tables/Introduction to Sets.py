# Introduction to Sets
# Sets are similar to dictionaries except that instead of having key/value pairs they only have the keys but not the values.

# Like dictionaries, they are implemented using a hash table (which is why we are covering them here).

# Sets can only contain unique elements (meaning that duplicates are not allowed). 

# They are useful for various operations such as finding the distinct elements in a collection and performing set operations such as union and intersection.

# They are defined by either using curly braces {} or the built-in set() function like this:



# Create a set using {}
my_set = {1, 2, 3, 4, 5}
 
# Create a set using set()
my_set = set([1, 2, 3, 4, 5])


# Once a set is defined, you can perform various operations on it, such as adding or removing elements, finding the union, intersection, or difference of two sets, and checking if a given element is a member of a set.

# Here are some examples of common set operations in Python:



# Add an element to a set
# If the number 6 is already in the set it will not be added again.
my_set.add(6)
 
# Update is used to add multiple elements to the set at once. 
# It takes an iterable object (e.g., list, tuple, set) as an 
# argument and adds all its elements to the set. 
# If any of the elements already exist in the set, 
# they are not added again.
my_set.update([3, 4, 5, 6])
 
# Removing an element from a set
my_set.remove(3)
 
# Union of two sets
other_set = {3, 4, 5, 6}
union_set = my_set.union(other_set)
 
# Intersection of two sets
intersection_set = my_set.intersection(other_set)
 
# Difference between two sets
difference_set = my_set.difference(other_set)
 
# Checking if an element is in a set
if "hello" in my_set:
    print("Found hello in my_set")

# You can learn more about sets by clicking here.

# Now let's look at some common coding interview questions that use sets!



