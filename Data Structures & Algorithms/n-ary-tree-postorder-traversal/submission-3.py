"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        self.arr = []
        
        def post(root):
            if root:
                for child in root.children:
                    post(child)
                self.arr.append(root.val)

        post(root)

        return self.arr