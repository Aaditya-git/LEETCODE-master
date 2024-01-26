'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1157520260/

''' 

class Solution(object):
    def maxProfit(self, prices):
        max_profit=0
        lowest=prices[0]
        for i in range(len(prices)):
            if prices[i]<lowest:
                lowest=prices[i]
            if prices[i]-lowest > max_profit:
                max_profit = prices[i]-lowest
        return max_profit
