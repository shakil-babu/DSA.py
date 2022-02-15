class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # addToBegin method

    def addToBegin(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            node.next = self.head
            return
        else:
            current = self.head
            while current.next != self.head:
                current = current.next

            current.next = node
            node.next = self.head
            self.head = node

    # addToEnd method
    def addToEnd(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            node.next = self.head
            return
        else:
            current = self.head
            while current.next != self.head:
                current = current.next

            current.next = node
            node.next = self.head

    # add after node

    def addAfterNode(self, val, newVal):
        node = Node(newVal)
        if self.head is None:
            self.head = node
            node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                if current.val == val:
                    break
                current = current.next

            if current.next == self.head:
                current.next = node
                node.next = self.head
            else:
                node.next = current.next
                current.next = node

            # search method
    def search(self, value):
        position = 0
        found = 0
        if self.head is None:
            print("The linked list does not exist")
        else:
            current = self.head
            while current:
                position = position + 1
                if current.val == value:
                    print("The required value was found at position: " + str(position))
                    found = 1
                    break
                if current.next == self.head:
                    break
                current = current.next
            if found == 0:
                print("The required value does not exist in the list")

    # delete from begin

    def deleteFromBegin(self):
        if self.head is None:
            print("Linked list is empty!")
            return
        else:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next

                self.head = self.head.next
                current.next = self.head

    # delete from end

    def deleteFromEnd(self):
        if self.head is None:
            print("Linked list is empty!")
            return
        else:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                prev = current
                while current.next.next != self.head:
                    current = current.next

                current.next = self.head

    # delete all nodes
    def deleteAllNodes(self):
        if self.head is None:
            print("List is emtpy!")
        else:
            cur = self.head
            while cur.next != self.head:
                temp = cur.next
                cur = None
                cur = temp
            self.head = None

    # count node

    def countNodes(self):
        count = 1
        if self.head is None:
            return 0
        else:
            cur = self.head
            while cur.next != self.head:
                count += 1
                cur = cur.next
            return count

    def PrintList(self):
        temp = self.head
        if(temp != None):
            print("The list contains:", end=" ")
            while (True):
                print(temp.val, end=" ")
                temp = temp.next
                if(temp == self.head):
                    break
        else:
            print("The list is empty.")


# initialization
cll = CircularSinglyLinkedList()
cll.addToBegin(10)
cll.addToBegin(20)
cll.addToEnd(100)
cll.addAfterNode(20, 200)
cll.PrintList()
print()
cll.deleteAllNodes()
print(cll.countNodes())
cll.PrintList()
