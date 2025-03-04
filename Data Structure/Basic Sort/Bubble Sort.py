# Bubble Sort
# Write a function called bubble_sort that sorts a list of integers in ascending order using the Bubble Sort algorithm.

# The function should perform the following tasks:

# Accept a parameter my_list that represents the list of integers to be sorted.

# Iterate through the list from the last element to the first element. For each element i, perform the following steps:

# Iterate through the list from the first element to the element at position i - 1. For each element j, perform the following steps:

# Compare the element at position j with the element at position j + 1. If the element at position j is greater than the element at position j + 1, swap the two elements.

# Return the sorted list.

## WRITE BUBBLE_SORT FUNCTION HERE ##
def bubble_sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
            


print(bubble_sort([4,2,6,5,1,3]))

 
 
"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """