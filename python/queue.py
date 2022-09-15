class Queue:

    def __init__(self, capacity):
        self.head = self.size = 0
        self.tail = capacity - 1
        self.Q = [None] * capacity
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def EnQueue(self, item):
        if self.isFull():
            print("Full")
            return
        self.tail = (self.tail + 1) % (self.capacity)
        self.Q[self.tail] = item
        self.size = self.size + 1
        print(str(item))

    def DeQueue(self):
        if self.isEmty():
            print("Empty")
            return
        print(str(self.Q[self.head]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size -1

    def que_front(self):
        if self.isEmpty():
            print("Empty")
        print(self.Q[self.head])

    def que_tail(self):

        if self.isEmpty():
            print("Empty")
        print(self.Q[self.rear])

if __name__ == "__main__":
    q = Queue(30)
    q.EnQueue(10)
    q.EnQueue(10)
    q.EnQueue(20)
    q.EnQueue(30)
    q.EnQueue(40)
    q.que_tail()
    q.que_head()

