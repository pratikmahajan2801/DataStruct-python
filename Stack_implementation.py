# Here we implement stack using arrays not list as list can dynamically grow and shrink.
import ctypes

class stack:                                        # Stack Class
    def __init__(self,capacity):
        self.top=-1
        self.stk=self.create_stkspace(capacity)

    def create_stkspace(self,capacity):
        return (capacity * ctypes.py_object)()


    def push(self,data):
        if(self.top==len(self.stk)-1):
            raise Exception("Stack Overflow")
        else:
            self.top+=1
            self.stk[self.top]=data


    def gettop(self):
        if(self.top==-1):
            raise Exception(" Empty stack no top")
        return self.stk[self.top]


    def pop(self):
        if(self.top<0):
            raise Exception("Stack Underflow")
        else:
            ret=self.gettop()
            self.stk[self.top]=0
            self.top-=1
            return ret


    def size(self):
        return self.top+1
    
    def print_stack(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Stack:")
            for i in range(self.top, -1, -1):
                print("|", self.stk[i], "|")
            print("-----")
    





