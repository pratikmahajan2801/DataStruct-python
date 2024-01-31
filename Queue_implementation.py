import ctypes

# Queue Implementation using arrays
class queue:
    def __init__(self,capacity):
        self.head=-1
        self.tail=-1
        self.size=0
        self.que=self.create_quespace(capacity)

    def create_quespace(self,capacity):
        return (capacity * ctypes.py_object)()

    def push(self,data):
        if(self.size>=len(self.que)):
            raise Exception("Queue full")
    
        if(self.size==0):
            self.head=0
            self.tail=0
            self.que[self.tail]=data
        else:
            self.tail=(self.tail+1) % len(self.que)
            self.que[self.tail]=data
        self.size+=1

    def pop(self):
        if(self.size<=0):
            raise Exception("Queue is already empty")
        
        x = self.que[self.head] 

        if(self.size==1):
            self.que[self.head]=0
            self.que[self.tail]=0
            self.head=-1
            self.tail=-1
        else:
            self.que[self.head]=0
            self.head=(self.head+1) % len(self.que)
        self.size-=1

        return x
    
    def top(self):
        if(self.head==-1):
            raise Exception("Queue empty...No top present")
        return self.que[self.head]

    def len(self):
        return self.size
    
    def print_queue(self):
        if self.head == -1:
            print("Queue is empty")
        else:
            print("Queue:")
            i = self.head
            while i != self.tail:
                print("|", self.que[i], end=" ")
                i = (i + 1) % len(self.que)
            print("|", self.que[self.tail], "|")
            

