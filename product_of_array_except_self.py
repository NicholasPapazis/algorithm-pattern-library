"""
Understand:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

Plan:
Build the result in two passes.
The first is a prefix pass and the second is the suffix pass.
The prefix pass will fill the output array with the product of all elements to the left of each index.
In the suffix pass, you walk from the right, keeping a running suffix product, and multiply it into each position.

"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        answer = [1]*n #create an array of the correct return length

        #prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        #suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer

# Time Complexity: O(n)
# Space Complexity: O(1) -> output array does not count
        