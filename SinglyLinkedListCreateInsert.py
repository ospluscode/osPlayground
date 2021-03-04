
# Create a singly linked list
# Insert to a singly linked list
# Time Complexity of creating linked list is O(1)
# Time Complexity of inserting is O(n)

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, value, location):
        newNode = Node(value)
        # no new node
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            # adding to beginning
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            # adding to end
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                # add middle
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode