class StackNode:
    def __init__(self, val = 0, left = None):
        self.val = val
        self.left = left


class Stack:
    def __init__(self):
        self.root = None
    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False
    def push(self, val):
        newNode = StackNode(val)
        newNode.next = self.root # inorder to make it as last node
        self.root = newNode
        print(f"{val} pushed to stack")
    def pop(self):
        if (self.isEmpty()):
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        popped = temp.val
        return popped
    def peek(self):
        if (self.isEmpty()):
            return float("-inf")
        return self.root.val
    def size(self):
        c = 0
        head = self.root
        while head != None:
            c += 1
            head = head.next
        return c


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.size()
    stack.pop()
    stack.peek()


