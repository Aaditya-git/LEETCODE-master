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
