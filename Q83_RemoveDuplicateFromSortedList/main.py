class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
    
def list_to_linkedlist(arr):
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

input_str = input("Enter sorted linked list values (space-separated): ")
arr = list(map(int, input_str.strip().split()))

head = list_to_linkedlist(arr)

sol = Solution()
new_head = sol.deleteDuplicates(head)

print("Linked list after removing duplicates:", linkedlist_to_list(new_head))
