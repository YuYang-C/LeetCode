# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
         t = dict()
         loc = 1
         t[loc] = head
         next_node = head.next
    
         # 只有一个元素，删除后必定返回None
         if next_node is None:
             return None
    
         while True:
             loc += 1
             t[loc] = next_node
    
             next_node = next_node.next
    
             if next_node is None:
                 break
    
         # 删除第一个
         if loc == n:
             head = t[2]
             return head
    
         # 删除最后一个
         if n == 1:
             t[loc-1].next = None
             return head
    
         t[loc-n].next = t[loc-n+2]
    
         return head
    
    
# 执行结果：通过
# 执行用时：28 ms, 在所有 Python3 提交中击败了99.50%的用户
# 内存消耗：13.6 MB, 在所有 Python3 提交中击败了5.72%的用户

