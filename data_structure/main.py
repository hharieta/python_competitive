from linked_list import LinkedList

def main():
    # start empty list
    llist = LinkedList()

    llist.append(6)
    llist.push_front(7)
    llist.push_front(1)
    llist.append(4)
    llist.push_back(llist.head.next, 8)

    print("Created list is: ")
    llist.print_list()



if __name__ == '__main__':
    main()