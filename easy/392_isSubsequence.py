'''
Code Link: https://leetcode.com/problems/is-subsequence/
'''

'''
Problem Statement :
Given two strings s and t, return true if s is a subsequence of t,
or false otherwise.
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lenS = len(s)
        lenT = len(t)
        i = 0
        j = 0

        #Traverse till end of the strings.
        while i<lenS and j<lenT:

            #Check character by character.
            if s[i] == t[j]:
                i = i + 1
            j+=1

        return i == lenS
