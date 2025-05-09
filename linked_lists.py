

# NODE CLASS FOR SINGLY LINKED LIST
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#NODE CLASS FOR DOUBLY LINKED LIST
class NodeDoubly:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# SINGLY LINKED LIST CLASS
class SinglyLinkedList:

    def __init__(self):
        self.head = None 

#appending a new node to the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:  
            self.head = new_node
            return
        curr = self.head
        while curr.next:  
            curr = curr.next
        curr.next = new_node

#inserting a new node at the beginning of the list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head  
        self.head = new_node  

#deleting the first node from the list
    def delete(self, data):
        if not self.head: 
            return
        if self.head.data == data:  
            self.head = self.head.next
            return
        curr = self.head
        while curr.next and curr.next.data != data:  
            curr = curr.next
        if curr.next:  
            curr.next = curr.next.next

#displaying the list
    def display(self):
        curr = self.head
        items = []
        while curr:
            items.append(str(curr.data))
            curr = curr.next
        return " -> ".join(items) if items else "Empty"

#searching for a node in the list
    def search(self, data):
        curr = self.head
        pos = 0
        while curr:
            if curr.data == data:
                return pos
            curr = curr.next
            pos += 1
        return -1
    

#DOUBLY LINKED LIST CLASS
class DoublyLinkedList:
    def __init__(self):
        self.head = None 
    def append(self, data):
        new_node = NodeDoubly(data)
        if not self.head:  
            self.head = new_node
            return
        curr = self.head
        while curr.next:  
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr  

#inserting a new node at the beginning of the list
    def prepend(self, data):
        new_node = NodeDoubly(data)
        if self.head:  
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

#deleting the first node from the list
    def delete(self, data):
        if not self.head: 
            return
        if self.head.data == data:  
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        curr = self.head
        while curr and curr.data != data: 
            curr = curr.next
        if curr: 
            if curr.prev:
                curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev

#display the list
    def display(self):
        curr = self.head
        items = []
        while curr:
            items.append(str(curr.data))
            curr = curr.next
        return " <-> ".join(items) if items else "Empty"

#searching for a node in the list
    def search(self, data):
        curr = self.head
        pos = 0
        while curr:
            if curr.data == data:
                return pos
            curr = curr.next
            pos += 1
        return -1



# TESTING THE LINKED LISTS
if __name__ == "__main__":
    print("Singly Linked List:")
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.prepend(0)
    print("List:", sll.display())
    print("Find 2:", sll.search(2))
    sll.delete(2)
    print("After delete 2:", sll.display())

    print("\nDoubly Linked List:")
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(0)
    print("List:", dll.display())
    print("Find 2:", dll.search(2))
    dll.delete(2)
    print("After delete 2:", dll.display())