# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit
# . Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# [2,4,3]
# [5,6,4]

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_llist(l):
    if l is None:
        return
    print(l.val)
    print_llist(l.next)


def addTwoNumbers(l1, l2, the_rem = 0):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    rem = 0
    if l1 is None and l2 is None:
        if the_rem != 0:
            return ListNode(the_rem)
        else:
            return
            
    if l1 is None:
        l1 = ListNode(0)


    if l2 is None:
        l2 = ListNode(0)


    the_sum = l1.val + l2.val + the_rem
    if the_sum > 9:
        the_sum %= 10
        rem = 1

    val = ListNode(the_sum)
    val.next = addTwoNumbers(l1.next, l2.next, the_rem = rem)
    return val

link1 = ListNode(2)
link1.next = ListNode(9)
link1.next.next  = ListNode(9)

link2 = ListNode(5)
link2.next =  ListNode(6)
link2.next.next  = ListNode(4)

res = addTwoNumbers(link1,link2)

print_llist(res)
