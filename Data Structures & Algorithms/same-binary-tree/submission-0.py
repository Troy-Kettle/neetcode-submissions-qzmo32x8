# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        self.state = True
        
        def inorder(root_a, root_b):
            if root_a and root_b:
                if root_a.val != root_b.val:
                    self.state = False
            elif not root_a and root_b:
                self.state = False
            elif root_a and not root_b:
                self.state = False


            if root_a and root_b:
                inorder(root_a.left, root_b.left)
                inorder(root_a.right, root_b.right)


                



        inorder(p, q)
        return self.state
                