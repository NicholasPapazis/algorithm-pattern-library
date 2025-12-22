"""
Understand:
Given two strings s and t, return true if t is an anagram of s,
and false otherwise.

Plan:
If lengths of s and t are not equal, then return false, as they can not be anagrams. 
Create map for both s and t maping their values to number of occurances.
Check for equality between the maps of s and t.

"""


class Solution(object):
    
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        mapS = {}
        mapT = {}
        
        if len(s) != len(t):
            return False

        for char, in s:
            mapS[char] = mapS.get(char, 0) + 1
        for char in t:
            mapT[char] = mapT.get(char, 0) + 1

        return mapS == mapT # order does not matter in comparison. 
    
# Time Complexity: O(n)
# Space Complexity: O(1) -> The dictionary can have at most 26 keys, no matter how long the string is.   


