# Queue implementation using stack
from Stack_implementation import stack

class stk_que:
    def __init__(self,capacity):
        self.stk1=stack(capacity)                   # Here we have used two stacks to form queue
        self.stk2=stack(capacity)
        self.cap=capacity
        self.size=self.stk1.size()
        
    def add(self,data):
        i=self.size
        if(self.size>=self.cap):
            raise Exception("Queue full")

        if(self.size==0):
            self.stk1.push(data)
        elif(self.size>0):
            while(i>0):
                self.stk2.push(self.stk1.pop())
                i-=1
            self.stk2.push(data)
            
            while(i<=self.size):
                self.stk1.push(self.stk2.pop())
                i+=1
        self.size+=1

    def rem(self):
        i=self.size
        if(i<=0):
            raise Exception("Queue empty")
        
        x= self.stk1.pop()
        self.size-=1
        return x

    def print_queue(self):
        if self.size == 0:
            print("Queue is empty")
        else:
            print("Queue:")
            for i in range(self.size - 1, -1, -1):
                print("|", self.stk1.stk[i], "|", end=" ")
            print()

        




