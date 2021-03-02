class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        if self.head == None:
            self.head = Node(data, None)
            self.size += 1
        else:
            new_node = Node(data, self.head)
            self.head = new_node
            self.size += 1

    def pop(self):
        if self.size == 1:
            self.head = None
            self.size -= 1
        else:
            self.head = self.head.next
            self.size -= 1

    def top(self):
        return self.head.data

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def __len__(self):
        return self.size

    def __contains__(self, value):
        itr_node = self.head

        while itr_node != None:
            if itr_node.data == value:
                return True
            itr_node = itr_node.next
        return False

    def __str__(self):
        itr_node = self.head

        str_stack = "["
        while True:
            if itr_node.next == None:
                str_stack += f"{str(itr_node.data)}"
                break
            str_stack += f"{str(itr_node.data)}, "
            itr_node = itr_node.next
        str_stack += "]"

        return str_stack

if __name__ == "__main__":
    obj = Stack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    obj.push(5)
    obj.push(6)
    print(obj)
    obj.pop()
    print(obj)
    print(len(obj))
    print(obj.top())
    print(obj.isEmpty())
    print(1 in obj)
    del obj