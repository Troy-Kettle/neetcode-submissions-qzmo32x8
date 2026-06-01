# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.state = True

        def inorder(root):
            if root:
                if abs(maxDepth(root.right) - maxDepth(root.left)) > 1:
                    self.state = False
                inorder(root.left)
                inorder(root.right)






        
        def maxDepth(root):
            if not root:
                return 0
            else:
                return 1 + max(maxDepth(root.left), maxDepth(root.right))

        inorder(root)

        return self.state