
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(0)        
        dummy.next = head
        curr = dummy
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next

def build_linked_list(nums):
    """Convert a Python list into a linked list."""
    if not nums:
        return None
    head = ListNode(nums[0])
    curr = head
    for n in nums[1:]:
        curr.next = ListNode(n)
        curr = curr.next
    return head

def linked_list_to_list(head):
    """Convert a linked list back into a Python list for easy printing."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

nums = input("Enter list elements separated by space: ").strip()
if nums:
    nums = list(map(int, nums.split()))
else:
    nums = []

val = int(input("Enter value to remove: "))

head = build_linked_list(nums)
solution = Solution()
new_head = solution.removeElements(head, val)

print("Updated linked list:", linked_list_to_list(new_head))
