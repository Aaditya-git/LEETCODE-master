'''
Code Link: https://leetcode.com/problems/isomorphic-strings/
'''

'''
Problem Statement :
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be
replaced to get t.All occurrences of a character must be replaced
with another character while preserving the order of characters.
No two characters may map to the samecharacter,
but a character may map to itself.
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
      # dictionary for stroing one to one mapping.
        diction = {}
        # use set to store value of already mapped characters
        setS = set()

        for i in range(len(s)):
            letterIns = s[i]
            letterInt = t[i]

            # if letter is already present.
            if letterIns in diction:
                # if the letter in already mapped, return False
                if diction[letterIns] != letterInt:
                    return False
            # if 'letterIns' is to be mapped for the first time.
            else:
                # if letterInt is previously mapped to other letterIns, return False
                if letterInt in setS:
                    return False
                # actual mapping ->
                diction[letterIns] = letterInt
                setS.add(letterInt)
        return True
