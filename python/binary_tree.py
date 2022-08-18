# iterative methods for pre-order, post-order, & in-order traversal
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root):
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
        

    def inorderTraversal(self, root):
        stack = []
        res = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                res.append(node.val)
                root = node.right
        return res


    def postorderTraversal(self, root):
        stack = []
        res = []
        while stack or root:
            if root:
                stack.append(root)
                res.append(root.val)
                root = root.right
            else:
                node = stack.pop()
                root = node.left
        return res[::-1]


    def levelorderTraversal(self, root):
        queue, res = deque([root]), []
        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                node = queue.popleft()
                if node: 
                    cur_level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if cur_level:
                res.append(cur_level)
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    t = Solution()
    print(t.preorderTraversal(root))
    print(t.inorderTraversal(root))
    print(t.postorderTraversal(root))
    print(t.levelorderTraversal(root))

