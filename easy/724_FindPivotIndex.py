'''
Code Link: https://leetcode.com/problems/find-pivot-index/
'''

'''
Problem Statement:
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the
left of the index is equal to the sum of all the numbers strictly to the index's
right. If the index is on the left edge of the array,then the left sum is 0 because
there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.
'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        Sum = 0
        Sum = sum(nums) #Total Sum

        sumL = 0
        sumR = Sum #Assign Total to right sum
        for i in range(0,len(nums)):
            sumR = sumR - nums[i] #Right sum shifting index by index.  

            if (sumL == sumR):
                return i
            sumL = sumL + nums[i]
        return -1
