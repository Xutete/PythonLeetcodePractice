import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class solution:


    def levelOrderBottom(self, root: TreeNode):

        result = []
        que = collections.deque()
        que.append(root)

        # while que is not empty
        while que:

            que_length = len(que)
            level = []


            # 需要在同一个level中
            for i in range(que_length):
                node = que.popleft()
                # print(node)

                if node:
                    level.append(node.val)
                    que.append(node.left)
                    que.append(node.right)

            # we want to make sure the level is non-empty
            if level:
                result.append(level)

        return result[: :-1]


    def levelOrderBottom2(self, root: TreeNode):

        if root is None:
            return []

        result = []
        current = [root]

        while current:
            next_level = []
            vals = []

            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level

            result.append(vals)

        return result[::-1]





