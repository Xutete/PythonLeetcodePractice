
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class solution:

    # NeetCode
    def levelOrder(self, root: TreeNode):

        result = []
        que = collections.deque()
        que.append(root)

        # while que is not empty
        while que:

            que_length = len(que)
            level = [] # 这里表示每一个while loop 开始 这个level 都清空为 []

            # if i in range(que_length) 说明循环还在同一个level中
            for i in range(que_length):
                node = que.popleft()

                # if node 是 none 则进入下一个 full 循环
                if node:
                    level.append(node.val)
                    que.append(node.left)
                    que.append(node.right)

            # we want to make sure the level is non-empty
            if level:
                result.append(level)

        return result



    # 代码随想录
    def levelOrder2(self, root: TreeNode):

        results = []

        if not root:
            return results

        from collections import deque
        que = deque([root])

        while que:
            size = len(que)
            result = []

            for _ in range(size):
                cur = que.popleft()
                result.append(cur.val)

                if cur.left:
                    que.append(cur.left)

                if cur.right:
                    que.append(cur.right)

            results.append(result)

        return results





