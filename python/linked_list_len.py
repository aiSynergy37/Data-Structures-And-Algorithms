# Findin the length of a linked list

class Node:

    def __init__(self, data = None, next = None):
        # node has two parts --- data and pointer to 
        # next node

        # node is an object 
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = Node()

    def append(self, new_data):
        new_node = Node(new_data)
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = new_node

    def display(self):
        curr_node = self.head
        i = 0
        while curr_node.next != None:
            curr_node = curr_node.next
            print(f"node_{i}_data",curr_node.data)
            i += 1

    def length(self):
        curr_node = self.head
        c = 0
        while curr_node.next != None:
            curr_node = curr_node.next
            c += 1

        print("\nlength of the LL : ", c)


def main():
    ll = LinkedList()
    ll.append(2)
    ll.append(3)
    ll.append(5)
    ll.append(11)
    ll.append(7)
    ll.display()
    ll.length()


if __name__ == "__main__":
    main()

