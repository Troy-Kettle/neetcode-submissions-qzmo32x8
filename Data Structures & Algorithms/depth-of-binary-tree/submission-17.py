# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        depth = 2

        if not root:
            return 0

        if root.left == None and root.right == None:
            return 1

        arr = []

        def right(root, depth1):
            depth1 += 1
            curr = root
            minNode(curr, depth1)

        def minNode(root, depth):
            if not root:
                return
            
            curr = root
            while True:
                if curr and curr.left and not curr.right:
                    curr = curr.left
                    depth += 1
                elif curr and curr.right and not curr.left:
                    curr = curr.right
                    depth += 1
                elif curr and curr.right and curr.left:
                    # carry on with left sub-tree
                    # then carry on with right sub-tree
                    right(curr.right, depth)
                    curr = curr.left
                    depth += 1
                    
                else:
                    break 
            arr.append((curr.val, depth))
            depth = 2

        # def maxNode(root):
        #     if not root:
        #         return
        #     depth = 0
        #     curr = root
        #     while True:
        #         if curr and curr.right:
        #             curr = curr.right
        #             depth += 1
        #         elif curr and curr.left:
        #             curr = curr.left
        #         else:
        #             break
        #     arr.append((curr.val, depth))

        minNode(root.left, depth)
        minNode(root.right, depth)
        
        # maxNode(root.left)
        # maxNode(root.right)

        deepest = 0
        for i in arr:
            if i[1] > deepest:
                deepest = i[1]

        print(arr)
        return deepest