# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        head.prev = None
        node = head
        while node.next:
            node.next.prev = node
            node = node.next
        pt1 = head
        pt2 = node

        while True:
            if pt1.val != pt2.val:
                return False
            else:
                pt1 = pt1.next
                pt2 = pt2.prev
            
            if pt1 == pt2 or pt1.prev == pt2:
                break
        return True