'''
Code Link: https://leetcode.com/problems/linked-list-cycle/
'''

'''
Problem Statement :
Given head, the head of a linked list, determine if the linked list has a cycle
in it.There is a cycle in a linked list if there is some node in the list that
can be reached again by continuously following the next pointer. Internally,
pos is used to denote the index of the node that tail's next pointer is
connected to. Note that pos is not passed as a parameter.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#VERY EASY NO NEED TO EXPLAIN!!!!!
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow,fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True



        return False
