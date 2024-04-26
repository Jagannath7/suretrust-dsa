class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None
        self.tail = None

    def add_at_tail(self, data):

        node = Node(data)

        if self.tail:
            # current tails points to new node
            self.tail.next = node

        # set new node as new tail
        self.tail = node

        if not self.head:
            self.head = node

    def add_at_head(self, data):

        node = Node(data)

        if not self.head:
            self.head = self.tail = node

        node.next = self.head
        self.head = node

    def print_list(self):

        temp = self.head

        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next

        print('\n')

    def insert_in_middle(self, data, position):

        if position == 0:
            self.add_at_head(data)
            return

        node = Node(data)
        temp = self.head
        i = 0
        while temp and i + 1 != position:
            i = i + 1
            temp = temp.next

        node.next = temp.next
        temp.next = node

    def search(self, key):

        temp = self.head
        i = 0
        while temp:
            if temp.data == key:
                return i
            temp = temp.next
            i += 1

        return -1

    def delete(self, key):

        temp = self.head
        prev = None

        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if prev is None:
            self.head = temp.next
            del temp
            return

        prev.next = temp.next

        if temp == self.tail:
            self.tail = prev

        del temp


ll = LinkedList()

ll.add_at_tail(10)
ll.add_at_tail(20)
ll.add_at_tail(30)
ll.add_at_tail(40)
ll.add_at_tail(50)

ll.insert_in_middle(70, 2)
ll.print_list()

ll.delete(10)
ll.delete(50)

ll.print_list()

print(ll.search(40))
