# Add Two Numbers II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack_1 = []
        stack_2 = []
        
        while l1:
            stack_1.append(l1.val)
            l1 = l1.next
        
        while l2:
            stack_2.append(l2.val)
            l2 = l2.next
            
        current = None
        total = 0
        while stack_1 or stack_2 or total:
            if stack_1:
                total += stack_1.pop()
            if stack_2:
                total += stack_2.pop()
                
            node = ListNode(total % 10)
            node.next = current
            current = node
            total = total // 10
        
        return current
        