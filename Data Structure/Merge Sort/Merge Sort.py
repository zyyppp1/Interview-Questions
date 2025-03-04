# Merge Sort
# Write a function called merge_sort that sorts a list of integers using the merge sort algorithm.

# The function should perform the following tasks:

# Accept a parameter, my_list, which represents the list of integers to be sorted.

# If the length of my_list is 1, return my_list as it is already sorted.

# Calculate the middle index of the list using integer division by 2 and store it in the variable mid_index.

# Recursively call the merge_sort function on the left and right halves of the list, created by slicing my_list using mid_index. Store the sorted left half in the variable left and the sorted right half in the variable right.

# Call the previously implemented merge function to combine the sorted left and right halves into a single sorted list.

# Return the sorted list.

def merge(array1, array2):
    combined = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            combined.append(array1[i])
            i += 1
        else:
            combined.append(array2[j])
            j += 1
              
    while i < len(array1):
        combined.append(array1[i])
        i += 1

    while j < len(array2):
        combined.append(array2[j])
        j += 1

    return combined


## WRITE MERGE_SORT FUNCTION HERE ##
def merge_sort(list):
    if len(list)==1:
        return list
    midindex=len(list)//2
    leftlist=merge_sort(list[:midindex])
    rightlist=merge_sort(list[midindex:])
    return merge(leftlist,rightlist)



original_list = [3,1,4,2]

sorted_list = merge_sort(original_list)

print('Original List:', original_list)

print('\nSorted List:', sorted_list)



"""
    EXPECTED OUTPUT:
    ----------------
    Original List: [3, 1, 4, 2]
    
    Sorted List: [1, 2, 3, 4]
    
 """