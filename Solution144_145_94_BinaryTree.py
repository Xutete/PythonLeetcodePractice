
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



class Solution:
    def preorderTraversal(self, root: TreeNode):
        # 保存结果
        result = []

        def traversal(root: TreeNode):
            if root == None:
                return

            result.append(root.val) # 前序
            traversal(root.left) # 左
            traversal(root.right) # 右

        traversal(root)
        return result


    def preorderTraversal2(self, root: TreeNode):
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def inorderTraversal(self, root: TreeNode):
        result = []

        def traversal(root: TreeNode):
            if root == None:
                return
            traversal(root.left)
            result.append(root.val)
            traversal(root.right)

        traversal(root)
        return result




    def inorderTraversal2(self, root: TreeNode):
        stack = []
        result = []

        while root is not None or stack != []:
            while root is not None:
                stack.append(root)
                root = root.left

            root = stack.pop()
            result.append(root.val)
            root = root.right()


        return result

    def postorderTraversal(self, root:TreeNode):
        result = []

        def traversal(root):

            if root == None:
                return

            traversal(root.left)
            traversal(root.right)
            result.append(root.val)

        traversal(root)

        return result



    def preoderTraversal3(self, root: TreeNode):
        result = []
        st = []

        if root:
            st.append(root)

        while st:
            node = st.pop()
            if node != None:
                if node.right: # 右
                    st.append(node.right)
                if node.left:  # 左
                    st.append(node.left)

                st.append(node) # 根
                st.append(None)

            else:
                node = st.pop()
                result.append(node.val)
        return result

    def inorderTraversal3(self, root: TreeNode):
        result = []
        st = []

        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node != None:
                if node.right: # 添加右节点 (空节点不入栈)
                    st.append(node.right) #

                st.append(node)  # 添加根节点
                st.append(None)  # 根节点访问过，但是没有处理，加入空节点作为标记

                if node.left:
                    st.append(node.left)

            else: # 只有遇到空节点的时候，才将下一个节点放入结果集
                node = st.pop()
                result.append(node.val) # 加入到结果集


        return result

    def postorderTraversal3(self, root: TreeNode):
        result = []
        st = []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node != None:
                st.append(node)  # 中
                st.append(None)

                if node.right:  # 右
                    st.append(node.right)
                if node.left:  # 左
                    st.append(node.left)
            else:
                node = st.pop()
                result.append(node.val)
        return result























