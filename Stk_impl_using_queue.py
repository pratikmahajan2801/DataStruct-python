# Here we implement stack using single queue
from Queue_implementation import queue

class que_stk:
    def __init__(self,capacity):
         self.que=queue(capacity)
         self.cap=capacity
         self.size=0
        
    
    def topp(self):
         if(self.size==0):
            raise Exception("Empty stack no top available") 
         return self.que.top()
    
    def pushh(self,data):
        if(self.size>=self.cap):
            raise Exception("Stack Overflow")
        i=self.size
        if(self.size==0):
            self.que.push(data)
        elif(self.size>0):
            self.que.push(data)
            while(i>0):
                x=self.que.pop()
                self.que.push(x)
                i-=1
        self.size+=1

    def popp(self):
        if(self.size<=0):
            raise Exception("Stack Underflow")
        x=self.que.pop()
        self.size-=1
        return x


