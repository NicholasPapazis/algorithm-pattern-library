"""
Understand:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day 
in the future to sell that stock.  
Return the miximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Plan:
You must buy before you sell.
Track the minimum price so far.
At each day, 
    pretent you sell today
    update max profit
update min price if today is cheaper

basically track the minimum price so far and update the maximum profit at each step. 


"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        #tracking lowest price and largest possible profit
        minPrice = float('inf')
        maxProfit = 0

        for price in prices:
            # finding the lowest price
            if price < minPrice: 
                minPrice = price
            # jumps here if next day price is larger than previous day price
            else: 
                maxProfit = max(maxProfit, price - minPrice) # determine largest between previous max profit, and new difference. 

        return maxProfit
        

# Time Complexity: O(n)
# Space Complexity: O(1)