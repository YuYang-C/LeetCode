# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def list_to_node(self, vals: list) -> ListNode:
        res = ListNode(vals[0])
        current_node = res
        for i in range(1, len(vals)):
            current_node.next = ListNode(vals[i])
            current_node = current_node.next
        return res

    def node_to_list(self, node):
        vals = list()
        vals.append(node.val)
        while (node.next!=None):
            vals.append(node.next.val)
            node = node.next
        return vals

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if(l1==None):
            return l2
        if(l2==None):
            return l1
        
        # list listnode's val and sort
        vals = list()
        vals = self.node_to_list(l1) + self.node_to_list(l2)
        vals.sort()
        
        # refctor listnode
        return self.list_to_node(vals)


if __name__ == '__main__':
    import sys
    aa = [1,2,5,8]
    bb = [1,2,4,9]
    if len(sys.argv) == 3:
        aa = eval(sys.argv[1])
        bb = eval(sys.argv[2])
    s = Solution()
    l1 = s.list_to_node(aa)
    l2 = s.list_to_node(bb)
    res = s.mergeTwoLists(l1, l2)
    print(f'l1 is {aa}, l2 is {bb}, res is {s.node_to_list(res)}')
