'''
Code Link: https://leetcode.com/problems/middle-of-the-linked-list/
'''

'''
Problem Statement :
Given the head of a singly linked list, return the middle node of the linked
list.If there are two middle nodes, return the second middle node.

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Classical Two Pointer Approach.
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first ,second = head, head

        # run untill second exist and second.next!= None (Imp)
        #otherwise second.next.next will look for element after None,
        #which is not possible hence the error.
        while second and second.next != None:
            second = second.next.next

            first = first.next

        # when 'second' reaches at the end, 'first' will manage to reach mid
        return first
