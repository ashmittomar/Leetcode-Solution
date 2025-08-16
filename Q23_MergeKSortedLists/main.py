import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        
        # Push head of each linked list into the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next

def build_linked_list(arr):
    """Convert list of numbers into a linked list."""
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def print_linked_list(head):
    """Print linked list as a list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

if __name__ == "__main__":
    k = int(input("Enter number of linked lists: "))
    lists = []
    
    for i in range(k):
        arr = input(f"Enter sorted elements of list {i+1} (space-separated, empty for []): ").strip()
        if arr == "":
            lists.append(None)
        else:
            arr = list(map(int, arr.split()))
            lists.append(build_linked_list(arr))
    
    solution = Solution()
    merged = solution.mergeKLists(lists)
    
    print("Merged Linked List:")
    print_linked_list(merged)
