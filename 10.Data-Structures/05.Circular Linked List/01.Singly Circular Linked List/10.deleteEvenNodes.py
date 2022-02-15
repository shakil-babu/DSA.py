

def deleteEvenNodes(self):
    if (self.head != None and self.head.next != self.head):
        # 1. if the list has more than one element
        #   create evenNode node - pointing to head
        #   oddNode node - pointing to next of head
        #   temp node - to store last odd node
        oddNode = self.head
        evenNode = self.head.next

        while(True):

            # 2. delete even node and update evenNode and
            #   oddNode to next set of odd-even nodes
            #   update temp node to latest oddNode node
            #   continue the process till any of the node
            #   reaches head
            temp = oddNode
            oddNode.next = evenNode.next
            evenNode = None
            oddNode = oddNode.next
            evenNode = oddNode.next
            if(oddNode == self.head or evenNode == self.head):
                break

        # 3. if oddNode reaches head, make next of
        #   temp as head else make next of oddNode
        #   as head
        if(oddNode == self.head):
            temp.next = self.head
        else:
            oddNode.next = self.head
