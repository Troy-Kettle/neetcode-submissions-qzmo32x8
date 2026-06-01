# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def preorder(root):
            if not root:
                return ["null"]
            return [root.val] + preorder(root.left) + preorder(root.right)


        arr1 = preorder(root)
        arr2 = preorder(subRoot)

        main = ",".join(map(str, arr1)) + ","
        sub = ",".join(map(str, arr2)) + ","

        result = any(main[i : i + len(sub)] == sub for i in range(len(main) - len(sub) + 1))

        return result