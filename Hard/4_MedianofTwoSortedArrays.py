'''
Code Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
'''

'''
Problem Statement :
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        #sort given array.
        array = nums1 + nums2
        array.sort()
        start = 0
        end = len(array)

        #finding Median
        if len(array)%2 == 0:
            tempMid = (start+end)//2
            secMid = tempMid - 1
            summ = array[tempMid] + array[secMid]
            return(summ/2)

        else:
            midd = (start + end)//2

            return array[midd]
