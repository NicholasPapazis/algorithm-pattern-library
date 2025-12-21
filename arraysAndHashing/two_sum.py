"""
Problem: 
Given an array of integers nums and an integer target, return
indicies of the two numbers such that they add up to target.  

Plan:
Create a map of value to index.
Loop through nums.  Inside loop have variable need 
equal target - current value.  If need is in map, 
the return an array of size two [component1, component2].
If need is not in the map, then add a new entry to the 
map containing current value and its index. 

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}
        for i, x in enumerate(nums):
            diff = target - x
            if diff in seen:
                return [seen[diff], i]
            seen[x] = i




# time complexity: O(n)
# space complexity: O(n)



