class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next


values = list(map(int, input("Enter linked list values (space-separated): ").split()))

dummy = ListNode(0)
current = dummy
for v in values:
    current.next = ListNode(v)
    current = current.next

head = dummy.next

n = int(input("Enter n (node from end to remove): "))

sol = Solution()
new_head = sol.removeNthFromEnd(head, n)

print("Updated linked list:")
temp = new_head
while temp:
    print(temp.val, end=" ")
    temp = temp.next
