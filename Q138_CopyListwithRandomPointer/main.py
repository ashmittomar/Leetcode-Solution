
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        
        if not head:
            return None

        # Step 1: Clone each node and insert it after the original node
        cur = head
        while cur:
            new_node = Node(cur.val, cur.next)
            cur.next = new_node
            cur = new_node.next

        # Step 2: Assign random pointers for cloned nodes
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # Step 3: Separate the original and cloned list
        cur = head
        new_head = head.next
        while cur:
            copy = cur.next
            cur.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            cur = cur.next

        return new_head


def build_linked_list(data):
    """Builds the linked list from input like [[7,null],[13,0],[11,4],[10,2],[1,0]]"""
    if not data:
        return None

    nodes = [Node(val) for val, _ in data]

    # set next pointers
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # set random pointers
    for i, (_, rand_index) in enumerate(data):
        if rand_index is not None:
            nodes[i].random = nodes[rand_index]

    return nodes[0]

def linked_list_to_array(head):
    """Convert linked list back to array format [[val, random_index], ...]"""
    if not head:
        return []

    mapping = {}
    arr = []
    cur = head
    index = 0

    # assign indices
    while cur:
        mapping[cur] = index
        cur = cur.next
        index += 1

    cur = head
    while cur:
        rand_index = mapping[cur.random] if cur.random else None
        arr.append([cur.val, rand_index])
        cur = cur.next
    return arr


if __name__ == "__main__":
    import ast
    user_input = input("Enter linked list (e.g. [[7,null],[13,0],[11,4],[10,2],[1,0]]): ")

    user_input = user_input.replace("null", "None")
    data = ast.literal_eval(user_input)

    head = build_linked_list(data)

    solution = Solution()
    new_head = solution.copyRandomList(head)

    print("Deep copied list:", linked_list_to_array(new_head))
