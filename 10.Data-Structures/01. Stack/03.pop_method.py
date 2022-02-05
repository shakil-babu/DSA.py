# pop method
def pop(self):
    if(len(self.data)):
        return self.data.pop()
    else:
        return "Pop failed!"
