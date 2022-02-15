class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


# singly linked list
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def Tail(self):
        print(self.tail.val)

    def len(self):
        print(self.length)

    # add to begin

    def addToBegin(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = self.head

        else:
            node.next = self.head
            self.head = node
        self.length += 1

    # print method

    def Print(self):
        if self.head is None:
            print("Linked list is emty!")
        else:
            current = self.head
            while current is not None:
                print(current.val, "--->", end=" ")
                current = current.next
            print("Null")

    # addToEnd method

    def addToEnd(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    # insertToIndex method

    def insertToIndex(self, val, index):
        if index <= 0 or self.length < index:
            print("Out of index!")
        else:
            node = Node(val)
            if self.head is None:
                self.head = node
                self.tail = self.head
            else:
                current = self.head
                count = 0
                while current.next is not None:
                    if count == index - 1:
                        break

                    current = current.next
                    count += 1
                temp = current.next
                current.next = node
                node.next = temp
                self.length += 1

    # deleteFromBegin method

    def deleteFromBegin(self):
        if self.head is None:
            print("Linked list is emty!")

        else:
            deleteNode = self.head
            self.head = deleteNode.next
            self.length -= 1

            if self.length == 0:
                self.tail = None

    # deleteFromEnd method

    def deleteFromEnd(self):
        if self.head is None:
            print("Linked list is emty!")

        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None
            self.length -= 1

    # deleteAnyNodeByValue method

    def deleteAnyNodeByValue(self, val):
        if self.head is None:
            print("Linked list is emty!")

        elif self.head.val == val:
            self.head = self.head.next
            self.length -= 1
        else:
            current = self.head
            while current.next is not None:
                if current.next.val == val:
                    break
                current = current.next

            if current.next is None:
                print("Node is not present!")

            else:
                current.next = current.next.next
                self.length -= 1

    # search method

    def search(self, val):
        if self.head is None:
            print("Linked list empty!")
        else:
            current = self.head
            while current is not None:
                if current.val == val:
                    return True
                current = current.next
            return False

    # getNode method

    def getNode(self, val):
        if self.head is None:
            print("Linked list empty!")
        else:
            current = self.head
            while current is not None:
                if current.val == val:
                    return current
                current = current.next

            return -1

    # setNode method

    def setNode(self, val, newValue):
        if self.head is None:
            print("Linked list is empty!")
        else:
            current = self.head
            while current is not None:
                if current.val == val:
                    current.val = newValue
                current = current.next

            return "Node not found!"

        # initialization
ll = SinglyLinkedList()
ll.addToBegin(300)
ll.addToBegin(220)
ll.addToEnd(900)
ll.Print()
print(ll.search(220))
ll.Print()
ll.len()
