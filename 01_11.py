# Convert Binary Number in a Linked List to Integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = []
        while head != None:
            binary.append(head.val)
            head = head.next

        rev_binary = binary[::-1]
        integer = 0
        for i in range(len(rev_binary)):
            integer += rev_binary[i] * (2 ** i)
        
        return integer
        