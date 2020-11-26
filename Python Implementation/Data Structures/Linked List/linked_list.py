import pysnooper

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
    
    def add_end(self, data):
        if self.empty():
            self.head = Node(data, None)
        else:
            iterate = self.head
            while iterate.next:
                iterate = iterate.next
            iterate.next = Node(data, None)

    def add_values_beginning(self, data_list):
        for data in data_list:
            self.add_beginning(data)

    def add_values_end(self, data_list):
        for data in data_list:
            self.add_end(data)   

    def __len__(self):
        counter = 0
        iterate = self.head
        while iterate:
            counter += 1
            iterate = iterate.next
        return counter


    def empty(self):
        return self.head == None

    def __str__(self):
        if self.empty():
            return "Linked List is empty."
        else:
            iterate = self.head
            iterate_str = ""
            
            while iterate:
                iterate_str += f"{iterate.data} --> "
                iterate = iterate.next
            return iterate_str

    
def main():
    data_list = [1,2,3,4,5,6,7]
    ll = LinkedList()
    ll.add_values_beginning(data_list)
    print(ll)
    ll2 = LinkedList()
    ll2.add_values_end(data_list)
    print(len(ll2))

    ll.add_beginning(5)
    ll.add_beginning(89)
    ll.add_beginning(14)
    ll.add_beginning(10)
    ll.add_end(100)
    print(len(ll))

if __name__ == "__main__":
    main()