
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None




class Solution:
    def preorderTravelsal(self, root: TreeNode) -> [int]:
        # 保存结果
        result = []

        def traversal(root: TreeNode):
            if root == None:
                return

            result.append(root.value) # 前序
            traversal(root.left) # 左
            traversal(root.right) # 右

        traversal(root)

        return result

    def levelOrder(self, root: TreeNode) -> [[int]]:
        """二叉树层序遍历迭代法"""
        result = []
        if not root: # 负负得正
            return result

        from collections import deque
        que = deque ([root])

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

            result.append(result)

        return result



