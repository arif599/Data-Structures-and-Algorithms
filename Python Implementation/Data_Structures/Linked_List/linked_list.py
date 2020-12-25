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

    def get_head_node(self):
        return self.head

    def add_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
    
    def add_end(self, data):
        if self.empty():
            self.head = Node(data, None)
        else:
            itr_node = self.head
            while itr_node.next:
                itr_node = itr_node.next
            itr_node.next = Node(data, None)

    def add_values_beginning(self, data_list):
        for data in data_list:
            self.add_beginning(data)

    def add_values_end(self, data_list):
        for data in data_list:
            self.add_end(data)   

    def insert(self, index, data, insert_after=False):
        if index < 0 or index > len(self):
            raise Exception("Index out of bounds.")

        if index == 0:
            self.add_beginning(data)
        else:
            indexCounter = 0
            itr_node = self.head

            while itr_node:
                if indexCounter == index - 1:
                    new_node = Node(data, itr_node.next)
                    itr_node.next = new_node
                    break
                
                itr_node = itr_node.next
                indexCounter += 1

    def insert_by_val(self, val, new_data):
        itr_node = self.head
        found_val = False

        while itr_node:
            if itr_node.data == val:
                new_node = Node(new_data, itr_node.next)
                itr_node.next = new_node
                found_val = True
                break
            itr_node = itr_node.next
        
        if not found_val:
            raise Exception("Value not found.")


    def remove(self, index):
        if index < 0 or index > len(self):
            raise Exception("Index out of bounds.")

        if index == 0:
            self.head = self.head.next
        else:
            itr_node = self.head
            indexCounter = 0
            while itr_node:
                if indexCounter == index - 1:
                    itr_node.next = itr_node.next.next
                    break
                itr_node = itr_node.next
                indexCounter += 1
    
    def remove_by_val(self, val):
        itr_node = self.head
        found_val = False

        while itr_node:
            if itr_node.next.data == val:
                itr_node.next = itr_node.next.next
                found_val = True
                break
            itr_node = itr_node.next

        if not found_val:
            raise Exception("Value not found.")


    def __len__(self):
        #O(n) but can be avoided by putting 'size' as a attribute in linkedlist
        counter = 0
        itr_node = self.head
        while itr_node:
            counter += 1
            itr_node = itr_node.next
        return counter

    def empty(self):
        return self.head == None

    def print_reverse(self, head_node=None, node=None):
        if head_node == None:
            node = self.head

        if node == None: 
            return
        else: 
            self.print_reverse(head_node=False, node=node.next) 
            print(f"{str(node.data)} -->", end = ' ') 
            
        
        #print(str(head_data))

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

    def delete(self):
        itr_node = self.head

        while itr_node:
            temp = itr_node.next

            del itr_node.next
            del itr_node.data

            itr_node = temp
    
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
    ll.add_end(100)
    print(ll)
    ll.insert(2, 69)
    print(ll)
    #ll.delete()
    ll.print_reverse()

    # ll.add_values_beginning(["banana","mango","grapes","orange"])
    # print(ll)
    # ll.insert_by_val("mango","apple") # insert apple after mango
    # print(ll)
    # ll.remove_by_val("mango")
    # print(ll)

if __name__ == "__main__":
    main()