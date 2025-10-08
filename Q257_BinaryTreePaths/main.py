# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        def dfs(node, path, res):
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                res.append("->".join(path))
            else:
                dfs(node.left, path[:], res)
                dfs(node.right, path[:], res)

        result = []
        dfs(root, [], result)
        return result


# Function to build a binary tree from level order input (like [1,2,3,null,5])
def build_tree(values):
    if not values or values[0] == "null":
        return None

    from collections import deque
    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1

    return root


print("Enter the tree in level order (use 'null' for empty nodes):")

user_input = input().split()

root = build_tree(user_input)

# Get all root-to-leaf paths
solution = Solution()
paths = solution.binaryTreePaths(root)

print("\nAll Root-to-Leaf Paths:")
for p in paths:
    print(p)
