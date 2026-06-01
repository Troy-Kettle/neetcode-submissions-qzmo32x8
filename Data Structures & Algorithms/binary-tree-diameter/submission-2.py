# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        longest = []
        
        
        def maxDepth(root):
            if not root:
                return 0
            return 1 + max(maxDepth(root.left), maxDepth(root.right))

        # Function to do in order tree traversal (a type of depth first search)
        def inorder(root, longest):
            
            if root:
                longest_path = maxDepth(root.left) + maxDepth(root.right)

                inorder(root.left, longest)
                inorder(root.right, longest)

                longest.append(longest_path)

        inorder(root, longest)

        return max(longest)
                