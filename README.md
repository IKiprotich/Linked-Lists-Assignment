# Linked List Assignment

## Overview

This project implements both **singly** and **doubly** linked lists in Python, showcasing common operations like insertion, deletion, searching, and displaying list contents.

---

## File: `linked_list.py`

### Classes

#### `Node`
Represents a node in a singly linked list.
- **Attributes:**
  - `data`: The value (e.g., a number).
  - `next`: A reference to the next node.

#### `DoublyNode`
Represents a node in a doubly linked list.
- **Attributes:**
  - `data`: The value.
  - `next`: A reference to the next node.
  - `prev`: A reference to the previous node.

#### `SinglyLinkedList`
A class for managing a singly linked list.
- **Methods:**
  - `append(value)`: Add a node to the end.
  - `prepend(value)`: Add a node to the beginning.
  - `delete(value)`: Remove the first node with the given value.
  - `search(value)`: Find the position (index) of a value in the list.
  - `display()`: Show the current list.

#### `DoublyLinkedList`
A class for managing a doubly linked list.
- **Methods:** (same as `SinglyLinkedList`)
  - `append(value)`
  - `prepend(value)`
  - `delete(value)`
  - `search(value)`
  - `display()`

---

## Test Cases

Both linked lists are tested with the following steps:

1. Append values: `1`, `2`, `3`
2. Prepend value: `0`
3. Display the list
4. Search for value `2`
5. Delete value `2`
6. Display the list again

---

## Sample Output
### Singly Linked List
- List: 0 -> 1 -> 2 -> 3
- Find 2: 2
- After delete 2: 0 -> 1 -> 3

### Doubly Linked List
- List: 0 <-> 1 <-> 2 <-> 3
- Find 2: 2
- After delete 2: 0 <-> 1 <-> 3

