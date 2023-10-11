class Node:
    # Function to initialize the node object
    def __init__(self, data: any):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


class LinkedList(Node): 
    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None

    # add a node at the front
    # 4 steps process
    def push_front(self, new_data: any) -> Node:
        #1 & 2: allocate the Node and put in the data
        new_node = Node(new_data)

        # 3: make next of new node as head
        new_node.next = self.head

        # 4: Move the head to point to new Node
        self.head = new_node
    

    # Add a node after a given node 5 steps
    def push_back(self, p_node, new_data):
        # 1: check if given p_node exists
        if p_node is None: 
            print("The given previous node must inLinkedList.") 
            return
        
        # 2: create new node and 3: put in the data
        new_node = Node(new_data)

        # 4: Make next of new Node as next of p_node
        new_node.next = p_node.next

        # 5: make next of p_node as new_node
        p_node.next = new_node
    

    def append(self, new_data):
        # 1: create node, 2: put in data, 3: set next as None
        new_node = Node(new_data)

        # 4: if the linked list is empty, then make
        # the new_node as head
        if self.head is None:
            self.head = new_node
            return
        
        # 5: Else traverse till the last node
        last = self.head
        while(last.next):
            last = last.next
        
        # 6: change the next of last node
        last.next = new_node
    

    # Utility function to print the linked list
    def print_list(self) -> Node:
        tmp = self.head
        while(tmp):
            print(tmp.data, end="")
            tmp = tmp.next

    

# if __name__ == '__main__':
#     # start empty list
#     llist = LinkedList()

#     llist.append(6)
#     llist.push_front(7)
#     llist.push_front(1)
#     llist.append(4)
#     llist.push_back(llist.head.next, 8)

#     print("Created list is: ")
#     llist.print_list()