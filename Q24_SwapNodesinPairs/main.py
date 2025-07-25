class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    curr = head
    for val in lst[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def linked_list_to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            first = current.next
            second = current.next.next

            first.next = second.next
            second.next = first
            current.next = second

            current = first

        return dummy.next

if __name__ == "__main__":
    user_input = input("Enter elements of the linked list separated by spaces: ")
    nums = list(map(int, user_input.strip().split()))

    head = create_linked_list(nums)
    sol = Solution()
    swapped_head = sol.swapPairs(head)

    output = linked_list_to_list(swapped_head)
    print("Swapped List:", output)
