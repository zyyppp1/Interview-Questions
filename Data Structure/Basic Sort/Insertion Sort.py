# Insertion Sort
# Write a function called insertion_sort that sorts a list of integers in ascending order using the Insertion Sort algorithm.

# The function should perform the following tasks:

# Accept a parameter my_list that represents the list of integers to be sorted.

# Iterate through the list from the second element to the last element. For each element i, perform the following steps:

# Store the value of the element at position i in a temporary variable called temp.

# Initialize another variable j to i - 1.

# While temp is less than the element at position j and j is greater than or equal to 0, perform the following steps:

# Move the element at position j to the position j + 1.

# Place the value of temp at position j.

# Decrement j by 1.

# Return the sorted list.

## WRITE INSERTION_SORT FUNCTION HERE ##
def insertion_sort(list):
    for i in range(1,len(list)):
        temp=list[i]
        j=i-1
        while temp<list[j] and j>-1:
            list[j+1]=list[j]
            list[j]=temp
            j-=1
    return list
print(insertion_sort([4,2,6,5,1,3]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """

