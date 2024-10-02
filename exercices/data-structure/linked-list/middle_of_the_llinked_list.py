"""
Solution for the problem:

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

source: https://leetcode.com/problems/middle-of-the-linked-list/
submission: https://leetcode.com/problems/middle-of-the-linked-list/submissions/1409732803/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head.next == None:
            return head

        if head.next.next == None:
            return head.next

        fast = head
        slow = head

        while slow:
            if fast == None or fast and fast.next == None:
                return slow
            fast = fast.next.next
            slow = slow.next