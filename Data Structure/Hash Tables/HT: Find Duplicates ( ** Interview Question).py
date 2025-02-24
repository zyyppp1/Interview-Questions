# HT: Find Duplicates ( ** Interview Question)
# find_duplicates()


# Problem: Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).


# Input:

# A list of integers nums.


# Output:

# A list of integers representing the numbers in the input array nums that appear more than once. If no duplicates are found in the input array, return an empty list [].



# Input: nums = [4, 3, 2, 7, 8, 2, 3, 1]
# Output: [2, 3]
# Explanation: The numbers 2 and 3 appear more than once in the input array.
 
# Input: nums = [1, 2, 3, 4, 5]
# Output: []
# Explanation: There are no duplicates in the input array, so the function returns an empty list [].
 
# Input: nums = [3, 3, 3, 3, 3]
# Output: [3]
# Explanation: The number 3 appears more than once in the input array.
 
# Input: nums = [-1, 0, 1, 0, -1, -1, 2, 2]
# Output: [-1, 0, 2]
# Explanation: The numbers -1, 0, and 2 appear more than once in the input array.
 
# Input: nums = []
# Output: []
# Explanation: There are no numbers in the input array, so the function returns an empty list [].

def find_duplicates(nums):
    count_dict = {}  # Dictionary to count occurrences
    output = []  # List to store duplicates
    
    for num in nums:
        if num in count_dict:  # If already seen before
            count_dict[num] += 1
        else:
            count_dict[num] = 1  # First occurrence

    # Collect numbers that appear more than once
    for num, count in count_dict.items():
        if count > 1:
            output.append(num)
    
    return output
            




print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

