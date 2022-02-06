# topElement method
def topElement(self):
    if(len(self.data)):
        return self.data[0]
    else:
        return "queue is empty!"
