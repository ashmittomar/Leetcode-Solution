from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

def build_tree(values):
    if not values:
        return None
    nodes = [None if val is None else TreeNode(val) for val in values]
    kids = deque(nodes[1:])
    for node in nodes:
        if node:
            if kids:
                node.left = kids.popleft()
            if kids:
                node.right = kids.popleft()
    return nodes[0]

# Helper function to print tree as list (level order)
def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
            
    while result and result[-1] is None:
        result.pop()
    return result

if __name__ == "__main__":
    user_input = input("Enter tree as list : ")
    values = eval(user_input)  
    root = build_tree(values)

    sol = Solution()
    inverted_root = sol.invertTree(root)

    print("Inverted tree:", tree_to_list(inverted_root))
