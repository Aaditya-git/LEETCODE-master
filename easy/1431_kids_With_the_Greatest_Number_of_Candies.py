'''
Problem link : https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75
'''



class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        peak = []
        max = candies[0]
        for i in range(len(candies)):
            if candies[i] > max:
                max = candies[i]
        for j in range(len(candies)):
            if (candies[j] + extraCandies) >= max:
                peak.append(True)
            else:
                peak.append(False)

        return peak


