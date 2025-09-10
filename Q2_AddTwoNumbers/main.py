
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10
            current.next = ListNode(new_val)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next


def build_linked_list(nums):
    """Convert Python list -> Linked list"""
    dummy = ListNode(0)
    current = dummy
    for n in nums:
        current.next = ListNode(n)
        current = current.next
    return dummy.next

def print_linked_list(node):
    """Print linked list as Python list"""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)


if __name__ == "__main__":
    # Example input: 2 4 3
    l1_nums = list(map(int, input("Enter digits for l1 (space-separated, reversed order): ").split()))
    l2_nums = list(map(int, input("Enter digits for l2 (space-separated, reversed order): ").split()))

    l1 = build_linked_list(l1_nums)
    l2 = build_linked_list(l2_nums)

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    print("Result linked list (reversed order):")
    print_linked_list(result)
