# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head

        node = prev = head

        while head is not None:
            if head.val == val:
                if head.next is not None:
                    head.val = head.next.val
                    head.next = head.next.next
                else:
                    prev.next = head = None
            else:
                prev = head
                head = head.next

        if node.val == val:
            node = None
        return node
