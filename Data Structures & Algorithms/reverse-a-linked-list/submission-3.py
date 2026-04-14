# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None 

        while curr:
            next_node = curr.next #备份节点
            curr.next = prev
            prev = curr #前移
            curr = next_node #前移
        
        return prev #新的头节点