# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        
        def helper(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        
        return helper(0, len(nums) - 1)


# Function to print tree in level order for visualization
from collections import deque
def printLevelOrder(root):
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            result.append(None)
    # Remove trailing Nones for clean output
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    nums = list(map(int, input("Enter sorted array elements separated by space: ").split()))
    sol = Solution()
    bst_root = sol.sortedArrayToBST(nums)
    print("Level order representation of BST:", printLevelOrder(bst_root))
