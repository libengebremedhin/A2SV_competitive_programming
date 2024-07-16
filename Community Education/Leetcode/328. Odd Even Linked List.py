# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i, cur = 1, head
        dummy, dummy2 = ListNode(), ListNode()
        tail, tail2 = dummy, dummy2
        
        while cur:
            if i % 2 != 0:
                tail.next = cur
                tail = tail.next
            else:
                tail2.next = cur
                tail2 = tail2.next
            i += 1
            cur = cur.next
        tail.next = dummy2.next
        tail2.next = None
        return dummy.next
                

        
