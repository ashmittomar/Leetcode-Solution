from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
       
        result = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)

        dfs(root)
        return result

#  Helper: build tree from list
def build_tree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    q = deque([root])
    i = 1

    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1

    return root

if __name__ == "__main__":
    inputs = [
        [1, None, 2, 3],
        [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9],
        [],
        [1]
    ]

    sol = Solution()
    for arr in inputs:
        root = build_tree(arr)
        print("Input:", arr)
        print("Postorder:", sol.postorderTraversal(root))
        print("----")
