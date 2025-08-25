# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
       
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# --------- USER INPUT PART ---------
def createLinkedList(values, pos):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    nodes = [head]  # keep track of nodes

    for val in values[1:]:
        node = ListNode(val)
        current.next = node
        current = node
        nodes.append(node)

    # create cycle if pos >= 0
    if pos != -1:
        current.next = nodes[pos]

    return head


if __name__ == "__main__":
    # Example input
    values = list(map(int, input("Enter linked list values (space separated): ").split()))
    pos = int(input("Enter pos (index to connect tail, -1 for no cycle): "))

    head = createLinkedList(values, pos)

    sol = Solution()
    print("Cycle Present?" , sol.hasCycle(head))
