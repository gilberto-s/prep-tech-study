"""
Solution for the problem:

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

source: https://leetcode.com/problems/linked-list-cycle/description/
submission: https://leetcode.com/problems/linked-list-cycle/submissions/1409834928
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False

        if head == head.next:
            return True

        current_node = head
        visited_nodes = []

        while current_node:
            if current_node.next == None:
                return False

            is_on_visited_nodes = visited_nodes.index(current_node) if current_node in visited_nodes else None
            if is_on_visited_nodes:
                return True

            visited_nodes.append(current_node)
            current_node = current_node.next