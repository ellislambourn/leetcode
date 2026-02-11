import heapq
# minheap

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [NodeWrapper(node) for node in lists if node] 
        if not lists:
            return None
        # the heap is a python list of node (nodewrapper so direct comparison can be made on node by heapq). i want the minimum which heapq does anyways.
        head = ListNode()
        curr = head
        heapq.heapify(heap)
        while heap:
            node = heapq.heappop(heap) # node is smallest node
            if node.node.next:
                heapq.heappush(heap, NodeWrapper(node.node.next))
            curr.next = node.node
            curr = curr.next

        return head.next
