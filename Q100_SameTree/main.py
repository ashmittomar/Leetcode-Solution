from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (p.val == q.val and 
                self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))

p_input = input("Enter tree p as list (e.g. [1,2,3]): ")
q_input = input("Enter tree q as list (e.g. [1,2,3]): ")

p_list = eval(p_input)
q_list = eval(q_input)

p_root = build_tree(p_list)
q_root = build_tree(q_list)

sol = Solution()
print("Trees are same:", sol.isSameTree(p_root, q_root))
