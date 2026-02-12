# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        length = self.getLength(head)
        if length == 1:
            return head
        

        curr = head
        head, kthNode = self.reverseKNodes(curr, k)
        count = k 
        while count < length:
            if length - count >= k:
                kthNode.next, newTail = self.reverseKNodes(kthNode.next, k)
                count += k
                kthNode = newTail
                
            else:
                break
        return head
            
        
    def getLength(self, head) -> int:
        count = 0
        curr = head
        while curr:
            count +=1
            curr = curr.next
        return count
        
    def reverseKNodes(self, head, k):
        prev = None
        curr = head

        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head.next = curr
        return prev, head
            


        