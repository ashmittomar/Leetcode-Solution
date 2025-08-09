from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val) and \
                   isMirror(t1.left, t2.right) and \
                   isMirror(t1.right, t2.left)
        
        return isMirror(root.left, root.right)

def build_tree_from_list(vals):
    if not vals:
        return None
    
    root = TreeNode(vals[0])
    queue = deque([root])
    i = 1
    n = len(vals)
    
    while queue and i < n:
        node = queue.popleft()
        
        if i < n and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        
        if i < n and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    
    return root

if __name__ == "__main__":
    input_str = input("Enter the tree nodes in level order, separated by commas (use 'null' for None): ")
    input_list = [int(x) if x.strip() != 'null' else None for x in input_str.split(',')]
    
    root = build_tree_from_list(input_list)
    
    sol = Solution()
    print(sol.isSymmetric(root))
