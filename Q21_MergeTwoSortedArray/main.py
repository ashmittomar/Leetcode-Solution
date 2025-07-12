class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    else:
        tail.next = list2

    return dummy.next

def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print("Merged Linked List:", result)

def get_user_input(prompt):
    try:
        values = list(map(int, input(prompt).strip().split()))
        return sorted(values)  # Ensure sorted input
    except:
        return []

if __name__ == "__main__":
    list1_values = get_user_input("Enter elements of first sorted list (space-separated): ")
    list2_values = get_user_input("Enter elements of second sorted list (space-separated): ")

    list1 = build_linked_list(list1_values)
    list2 = build_linked_list(list2_values)

    merged = merge_two_lists(list1, list2)
    print_linked_list(merged)
