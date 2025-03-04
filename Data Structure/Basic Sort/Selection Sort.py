# Selection Sort
# Write a function called selection_sort that sorts a list of integers in ascending order using the Selection Sort algorithm.

# The function should perform the following tasks:

# Accept a parameter my_list that represents the list of integers to be sorted.

# Iterate through the list from the first element to the second-to-last element. For each element i, perform the following steps:

# Set min_index to the index of the current element i.

# Iterate through the list from the element at position i + 1 to the last element. For each element j, perform the following steps:

# Compare the element at position j with the element at position min_index. If the element at position j is less than the element at position min_index, update min_index to the index j.

# If the index i is not equal to min_index, swap the elements at positions i and min_index.

# Return the sorted list.

## WRITE SELECTION_SORT FUNCTION HERE ##
def selection_sort(list):
    for i in range(len(list)-1):
        minindex=i
        for j in range(i,len(list)):
            if list[j]<list[minindex]:
                minindex=j
        list[i],list[minindex]=list[minindex],list[i]
    return list

print(selection_sort([4,2,6,5,1,3]))


 
"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """

