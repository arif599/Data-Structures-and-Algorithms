"""
TODO: 
- Add counter attribute for O(1)
- Add tail pointer so that adding element to the end takes O(1)
- Add isEmpty and isFull
- use proper encapsulation, seters, and getters
"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        count = 0

    def get_head_node(self):
        return self.head.data

    def get_tail_node(self):
        return self.tail.data

    def add_beginning(self, data):
        new_node = Node(data, self.head)
        if self.empty():
            self.tail = new_node
        self.head = new_node

    
    def add_end(self, data):
        new_node = Node(data, None)
        self.tail.next = new_node
        self.tail = new_node 

    def empty(self):
        return self.head == None

    def __str__(self):
        if self.empty():
            return "Linked List is empty."
        else:
            itr_node = self.head
            itr_node_str = ""
            
            while itr_node:
                itr_node_str += f"{itr_node.data} --> "
                itr_node = itr_node.next

            return itr_node_str

    
def main():
    ll = LinkedList()
    # data_list = [1,2,3,4,5,6,7]
    # ll.add_values_beginning(data_list)
    # print(ll)
    # ll2 = LinkedList()
    # ll2.add_values_end(data_list)
    # print(ll2)

    ll.add_beginning(5)
    ll.add_beginning(89)
    ll.add_beginning(14)
    ll.add_beginning(10)
    ll.add_end(1)
    print(ll.get_tail_node())
    
    # ll.add_end(100)
    # print(ll)
    # ll.insert(2, 69)
    # print(ll)
    # #ll.delete()
    # ll.print_reverse()

    # ll.add_values_beginning(["banana","mango","grapes","orange"])
    # print(ll)
    # ll.insert_by_val("mango","apple") # insert apple after mango
    # print(ll)
    # ll.remove_by_val("mango")
    # print(ll)

if __name__ == "__main__":
    main()