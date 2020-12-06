# https://leetcode-cn.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next# class Solution:


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

    def _add_two_num_with_carry(self, v1: int, v2: int, carry: int) -> tuple:
         res = v1 + v2 + carry

         return (1, res -10)  if res -10 >= 0 else (0, res)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
         carry = 0

         carry, res_val = self._add_two_num_with_carry(l1.val, l2.val, carry)
         org = res = ListNode(res_val)

         l1 = l1.next
         l2 = l2.next
        
         while True:
             if l1 is None and l2 is None:
                 break

             v1 = v2 = 0

             if l1 is not None:
                 v1, l1 = l1.val, l1.next

             if l2 is not None:
                 v2, l2 = l2.val, l2.next

             carry, res_val = self._add_two_num_with_carry(v1, v2, carry)
             res.next = ListNode(res_val)

             res = res.next

         if carry:
             res.next = ListNode(carry)
        
         return org

if __name__ == '__main__':
    import sys

    aa = [2, 4, 3]
    bb = [5, 6, 4]

    if len(sys.argv) == 3:
        aa = eval(sys.argv[1])
        bb = eval(sys.argv[2])

    s = Solution()

    l1 = s.list_to_node(aa)
    l2 = s.list_to_node(bb)

    res = s.addTwoNumbers(l1, l2)

    print(f'l1 is {aa}, l2 is {bb}, res is {s.node_to_list(res)}')


# 执行结果：通过

# 执行用时：76 ms, 在所有 Python3 提交中击败了72.83%的用户

# 内存消耗：13.5 MB, 在所有 Python3 提交中击败了30.75%的用户
