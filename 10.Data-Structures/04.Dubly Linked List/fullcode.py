# node blueprint
class Node:
    def __init__(self, val=None):
        self.prev = None
        self.val = val
        self.next = None


# Dubly Linked List
class DublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # addToBegin method
    def addToBegin(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.length += 1

    # addToEnd method
    def addToEnd(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    # insertAfterNode
    def insertAfterNode(self, val, newVal):
        node = Node(newVal)
        if self.head is None:
            print("DLL is empty!")
        else:
            current = self.head
            while current is not None:
                if current.val == val:
                    break
                current = current.next

            if current is None:
                print("Node is not found!")
            else:
                node.next = current.next
                node.prev = current

                if current.next is not None:
                    current.next.prev = node
                current.next = node

    # print method

    def print(self):
        if self.head is None:
            print("DLL is empty!")
        else:
            current = self.head
            print("Null --> ", end='')
            while current is not None:
                print(current.val, end="--> ")
                current = current.next
            print("Null")

    # search an item

    def search(self, item):
        if self.head is None:
            print("DLL is empty!")
        else:
            current = self.head
            while current is not None:
                if current.val == item:
                    return True
                current = current.next
            if current is None:
                return False

    # insert before node

    def insertBeforeNode(self, val, newVal):
        node = Node(newVal)
        if self.head is None:
            print("DLL is empty!")
        else:
            current = self.head
            while current is not None:
                if current.val == val:
                    break
                current = current.next

            if current is None:
                print("Node is not found!")
            else:
                node.next = current
                node.prev = current.prev

                if current.prev is not None:
                    current.prev.next = node
                else:
                    self.head = node
                current.prev = node

    # delete from begin

    def deleteFromBegin(self):
        if self.head is None:
            print("Dll is empty!")
            return

        if self.head.next is None:
            self.head = None
            self.tail = None

        else:
            current = self.head
            self.head = current.next
            current.prev = None

        self.length -= 1

    # delete from end

    def deleteFromEnd(self):
        if self.head is None:
            print("Dll is empty!")
            return

        if self.head.next is None:
            self.head = None
            self.tail = None

        else:
            current = self.head
            while current.next.next is not None:
                current = current.next

            current.next = None

    # delete by value
    def deleteByValue(self, val):
        if self.head is None:
            print("Dll is empty!")
            return

        if self.head.next is None:
            if self.head.val == val:
                self.head = None
                self.tail = None
            else:
                print("Node not found!")
            return

        if self.head.val == val:
            self.head = self.head.next
            self.head.prev = None

        else:
            current = self.head
            while current is not None:
                if current.val == val:
                    break
                current = current.next
            if current.next is not None:
                current.next.prev = current.prev
                current.prev.next = current.next
            else:
                if current.val == val:
                    current.prev.next = None
                else:
                    print("Node not present!")

    # set method
    def setValue(self, val, newVal):
        if self.head is None:
            print("Dll is empty!")
            return

        current = self.head
        while current is not None:
            if current.val == val:
                current.val = newVal
                break
            current = current.next


# initialization
dll = DublyLinkedList()
dll.addToBegin(10)
dll.addToEnd(20)
dll.addToEnd(30)
dll.setValue(30, 300)
dll.print()
