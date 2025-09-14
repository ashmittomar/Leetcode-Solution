from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if not node:
                return
            result.append(node.val)   # Root
            dfs(node.left)            # Left
            dfs(node.right)           # Right

        dfs(root)
        return result

# Helper to build tree from list
def build_tree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

if __name__ == "__main__":
    arr = input("Enter tree as list (use 'null' for None): ").replace("null", "None")
    arr = eval(arr)  
    root = build_tree(arr)

    sol = Solution()
    print("Preorder Traversal:", sol.preorderTraversal(root))
