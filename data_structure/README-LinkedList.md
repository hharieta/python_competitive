# [Introduction to Linked List – Data Structure and Algorithm Tutorials](https://www.geeksforgeeks.org/introduction-to-linked-list-data-structure-and-algorithm-tutorial/)

 ```text
 A Linked List is a linear data structure which looks like a chain of nodes, where each node is a different element. Unlike Arrays, Linked List elements are not stored at a contiguous location. 
```

It is basically chains of nodes, each node contains information such as data and a pointer to the next node in the chain. In the linked list there is a head pointer, which points to the first element of the linked list, and if the list is empty then it simply points to null or nothing.

---

## Singly-linked list

Traversal of items can be done in the forward direction only due to the linking of every node to its next node.

![Singly-linked](../assest/Singlelinkedlist.png)

```python3

class Node:
  
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
  

# Linked List class  
class LinkedList:
  
    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None

```
