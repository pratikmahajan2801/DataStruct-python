import ctypes

class darray:
    def __init__(self):
        self.size=1
        self.alloc=0
        self.arr=self.create_arr(self.size)

    def create_arr(self,capacity):
        return (capacity * ctypes.py_object)()


    def grow_shrink(self,new_cap):
        temp=self.create_arr(new_cap)
        self.size=new_cap

        for i in range (self.alloc):
            temp[i]=self.arr[i]

        self.arr=temp


    def append(self,data):
        if (self.size==self.alloc):
            self.grow_shrink(self.size*2)

        self.arr[self.alloc]=data
        self.alloc=self.alloc+1


    def size_cnt(self):
        return self.alloc
    

    def insert(self,data,ind):
        if (self.size==self.alloc):
            self.grow(self.size*2)

        for i in range(self.alloc-1,ind-1,-1):
            self.arr[i+1]=self.arr[i]
        
        self.arr[ind]=data
        self.alloc+=1
            

    def pop(self):
        self.arr[self.alloc-1]=0
        self.alloc-=1
        if self.alloc==(self.size//2):
            self.grow_shrink(self.alloc)

    def delete(self,ind):
        if ind==self.alloc-1:
            self.pop()
            return
        
        for i in range(ind,self.alloc-1):
            self.arr[i]=self.arr[i+1]
        self.arr[self.alloc-1]=0
        self.alloc-=1

    def print_array(self):
        print(self.arr[:self.alloc])
    

