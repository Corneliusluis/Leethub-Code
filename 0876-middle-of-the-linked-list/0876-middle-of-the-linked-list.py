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
        
        # still not sure how this works
        fast = slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
        