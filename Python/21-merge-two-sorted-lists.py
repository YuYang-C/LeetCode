# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if(l1==None):
            return l2
        if(l2==None):
            return l1
        
        # list listnode's val and sort
        vals = list()
        for l in (l1, l2):
            vals.append(l.val)
            while (l.next!=None):
                vals.append(l.next.val)
                l = l.next
        vals.sort()
        
        # refctor listnode
        res = ListNode(vals[0])
        current_node = res
        for i in range(1, len(vals)):
            current_node.next = ListNode(vals[i])
            current_node = current_node.next 
        return res
