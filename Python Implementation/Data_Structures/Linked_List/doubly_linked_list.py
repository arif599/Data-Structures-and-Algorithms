class Node:
    def __init__(self, previous=None, data=None, next=None):
        self.previous = previous
        self.data = data
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_beginning(self, data):
        new_node = Node(None, data, self.head)

        if self.head == None:
            self.head = new_node
            self.tail = new_node

        self.head.previous = new_node
        self.head = new_node

    def add_tail(self, data):
        new_node = Node(self.tail, data, None)

        if self.tail == None:
            self.head = new_node
            self.tail = new_node

        self.tail.next = new_node
        self.tail = new_node

    def print_forward(self):
        itr_node = self.head
        itr_node_str = ""

        while itr_node:
            itr_node_str += f"{itr_node.data} --> "
            itr_node = itr_node.next

        print(itr_node_str) 

    def print_backward(self):
        itr_node = self.tail
        itr_node_str = ""

        while itr_node:
            itr_node_str += f"{itr_node.data} --> "
            itr_node = itr_node.previous

        print(itr_node_str) 

dll = DoublyLinkedList()
dll.add_beginning(5)
dll.add_beginning(89)
dll.add_beginning(14)
dll.add_beginning(10)
dll.add_tail(100)
dll.print_forward()
dll.print_backward()