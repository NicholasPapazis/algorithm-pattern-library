"""
Problem:
Given an integer array nums, return true if any value appears at least twice in the array, and return false
if every element is distinct. 

Plan:
Create a list, loop through nums, if current number is in the list, return true, outside of loop return false. 

"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
      
        seen = []
        for i in nums:
            if i in seen:
                return True
            seen.append(i)
        return False

    # Time Complexity: O(n^2)
    # Space Complexity: O(n)



