class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        
        # Find left height
        left_height = 0
        left_node = root
        while left_node:
            left_height += 1
            left_node = left_node.left
        
        # Find right height
        right_height = 0
        right_node = root
        while right_node:
            right_height += 1
            right_node = right_node.right
        
        # If perfect binary tree
        if left_height == right_height:
            return (1 << left_height) - 1
        
        # Otherwise count recursively
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    

def build_tree(values):
    if not values or values[0] == "null":
        return None
    
    root = TreeNode(int(values[0]))
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        # Left child
        if i < len(values) and values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1
    
    return root


values = input("Enter tree nodes in level order (use 'null' for empty): ").split()
root = build_tree(values)

obj = Solution()
print("Total nodes in the tree:", obj.countNodes(root))
