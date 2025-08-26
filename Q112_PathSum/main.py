from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        if not root.left and not root.right:  # Leaf
            return targetSum == root.val
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))

# Function to build tree from list (level-order input like LeetCode)
def buildTree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

# -------- User Input --------
# Example: root = [5,4,8,11,None,13,4,7,2,None,None,None,1], targetSum = 22
arr = list(eval(input("Enter tree as list (use None for null): ")))
target = int(input("Enter target sum: "))

root = buildTree(arr)
sol = Solution()
print("Output:", sol.hasPathSum(root, target))
