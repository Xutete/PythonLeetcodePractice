
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right



class solution:
    def rightSideView(self, root: TreeNode):

        def dfs(node, res, depth):
            if node is None:
                return

            if len(res) == depth:
                res.append(node.val)

            dfs(node.right, res, depth + 1)
            dfs(node.left, res, depth + 1)

        res = []
        dfs(root, res, 0)

        return res




x = 1
x = "WF"
