
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

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

        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

class Solution(object):
    def inorderTraversal(self, root):
        result = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)
        return result

if __name__ == "__main__":
    user_input = input("Enter tree as comma-separated values (use 'null' for None): ")
    user_input = user_input.strip().split(',')
    
    tree_values = [int(x) if x.strip().lower() != 'null' else None for x in user_input]

    root = build_tree(tree_values)
    sol = Solution()
    result = sol.inorderTraversal(root)
    print("Inorder Traversal:", result)
