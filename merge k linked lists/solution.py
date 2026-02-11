# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not any(lists): # if no lists
            return None
        # this is the case for merging two lists
        head = ListNode()
        prev = head
        currNodes = [node for node in lists if node]



        while any(currNodes):
            # find lower of these.
            prev.next = min(currNodes,  key= lambda node: node.val)
            i = currNodes.index(prev.next)

            prev = prev.next


            # this keeps all nodes in currNodes active
            if currNodes[i].next is None:
                currNodes.pop(i)
            else:
                currNodes[i] = currNodes[i].next
        return head.next