# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


# Function to create linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Function to print linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)


values = list(map(int, input("Enter linked list elements separated by space: ").split()))

# Create the linked list
head = create_linked_list(values)

# Reverse using Solution class
sol = Solution()
reversed_head = sol.reverseList(head)

# Print reversed linked list
print("Reversed linked list:")
print_linked_list(reversed_head)
