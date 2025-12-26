"""
Understand:
We are given a string s, and we have to determine if it is a palindrome, after removing all non-alphanumeric characters. 


Plan:
keep track of l pointer and r ponter.
while they have not crossed
skip all non-alpanumeric characters
if left and right pointers are not equal, return false.
if outer loop completes return true. 


"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # pointers
        left, right = 0, len(s) - 1

        #controlling loop, make sure pointers have not crossed. 
        while left < right:

            # skips non-alphanumeric chars
            while left < right and not s[left].isalnum():
                left += 1

            # skips non-alphanumeric chars
            while left < right and not s[right].isalnum():
                right -= 1

            # if semetrical pointers are not equal, then s is not a palindrome
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        # If loop completes then s is an anagram
        return True 