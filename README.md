Linked List Assignment
What the Code Does
We have three classes in linked_list.py:

Node: Used for the singly linked list. It holds data (like a number) and a link to the next node.
DoublyNode: Used for the doubly linked list. Each node holds data and links to both the next and previous nodes.
SinglyLinkedList: This is a singly linked list. It can:
append: Add a node to the end.
prepend: Add a node to the start.
delete: Remove a node with a certain value.
display: Show the whole list.
search: Find where a value is in the list.


DoublyLinkedList: This is the doubly linked list. It does the same stuff as the singly linked list, but nodes are connected both ways (forward and backward).

The code has a test part at the end that tries out both lists by:

Adding the numbers 1, 2, and 3.
Adding 0 at the start.
Showing the list.
Finding where 2 is.
Deleting 2 and showing the list again.

Results from the Code
Singly Linked List:
List: 0 -> 1 -> 2 -> 3
Find 2: 2
After delete 2: 0 -> 1 -> 3

Doubly Linked List:
List: 0 <-> 1 <-> 2 <-> 3
Find 2: 2
After delete 2: 0 <-> 1 <-> 3

The singly linked list uses -> to show nodes pointing forward. The doubly linked list uses <-> because nodes link both ways. The “Find 2: 2” means 2 is at position 2 (starting from 0). After deleting 2, the lists are just 0, 1, and 3.
