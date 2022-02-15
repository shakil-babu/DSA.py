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
