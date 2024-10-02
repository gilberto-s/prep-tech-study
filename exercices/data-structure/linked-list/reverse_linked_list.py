"""
Solution for the problem:

Given the head of a singly linked list, reverse the list, and return the reversed list.

source: https://leetcode.com/problems/reverse-linked-list/description/
submission: https://leetcode.com/problems/reverse-linked-list/submissions/1409870965
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or head.next == None:
            return head

        previous_node = None

        while head:
            temp_node = head.next
            head.next = previous_node
            previous_node = head
            head = temp_node

        return previous_node