"""
Understand:
Given an unsorted array of integers num, return the length of the longest consecutive elements sequence. 

You must write an algorithm that runs in O(n) time. 

Plan:
Put elements of nums into a set(). This allows for efficient lookup O(1), and removes duplicates.
Iterate through that set, 
if curr-1 not in set, then curr is the start of a sequence. 
while curr+1 is in the set, increment length of the sequence. 
After loop completes, return the number representing the longest sequence. 


"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        num_set = set(nums) #convert nums into hashset for constant lookup time, and remove duplicates
        longest = 0 # keep track of longest sequence, as there may be more than one sequence of consecutive numbers in nums. 

        for num in num_set:
            if num-1 not in num_set: # if true, then this is the first element of a sequence. 
                curr = num # store num so we can keep checking the sequence
                length = 1 #tracks length of curent sequence. 
            
                while curr+1 in num_set:
                    curr += 1 #since curr+1 is in the sequence, we must increment curr to match the corresponding element in num_set
                    length += 1 

                longest = max(longest, length) #if length of current sequence is greater than longest, (meaning any previous sequences in nums) update longest to reflect that.  

        return longest

# Time Complexity: O(n)
# Space Complexity: O(n) -> set() grows with size of distinct elements in nums.
        