class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        before_head = ListNode(0)  # Dummy node
        before = before_head
        after_head = ListNode(0)
        after = after_head
        
        current = head
        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next
        
        after.next = None  # End list
        before.next = after_head.next  # Link two lists
        
        return before_head.next


def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


arr = list(map(int, input("Enter list elements separated by space: ").split()))
x = int(input("Enter x: "))

head = build_linked_list(arr)
solution = Solution()
new_head = solution.partition(head, x)

print("Output:", linked_list_to_list(new_head))
