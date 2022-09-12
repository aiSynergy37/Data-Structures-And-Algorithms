class TreeNode:
    def __init__(self, val = 0, p = None, left = None, right = None):
        self.val = val
        self.p = p
        self.left = left
        self.right = right


class Solution:
    def minimum(self, root):
        if root == None:
            return
        while root.left != None:
            root = root.left
        return root

    def treeSuccessor(self, x):
        if x == None:
            return
        if x.right != None:
            return self.minimum(x.right)
        y = x.p
        while y != None and x == y.right:
            x = y
            y = y.p
        return y

    def treeInsert(self, root, z):
        y = None
        x = root
        while x != None:
            y = x
            if z.val < x.val:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            root = z
        elif (z.val < y.val):
            y.val = z
        else:
            y.right = z
    
    def treeSearch(self, root, k):
        if root == None or root.val == k:
            return root
        if k < root.val:
            return self.treeSearch(root.left, k)
        else:
            return self.treeSearch(root.right, k)

    def iterativeTreeSearch(self, root, k):
        while x != None and k != x.val:
            if k < root.val:
                root = root.left
            else:
                root = root.right
        return x

    def treeMinimum(self, root):
        while root.left != None:
            root = root.left
        return root

    def treeMaximum(self, root):
        while root.right != None:
            root = root.right
        return root

    def inorderWalk(self, root):
        if root != None:
            self.inorderWalk(root.left)
            print(root.val)
            self.inorderWalk(root.right)
