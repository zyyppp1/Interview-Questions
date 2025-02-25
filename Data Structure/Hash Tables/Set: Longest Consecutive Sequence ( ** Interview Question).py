# Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).

# Use sets to optimize the runtime of your solution.

# Input: An unsorted array of integers, nums.

# Output: An integer representing the length of the longest consecutive sequence in nums.

# Example:



# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive sequence in the input array is [4, 3, 2, 1], and its length is 4.
# WRITE LONGEST_CONSECUTIVE_SEQUENCE FUNCTION HERE #
def longest_consecutive_sequence(nums):
    num_set=set(nums)
    longest_sequence=0
    for i in nums:
        if i-1 not in num_set:
            currentnum=i
            count=1

            while currentnum+1 in num_set:
                currentnum=currentnum+1
                count+=1

            longest_sequence=max(count,longest_sequence)

    return longest_sequence



print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""