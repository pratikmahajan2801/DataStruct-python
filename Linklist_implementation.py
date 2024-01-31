class node:                                         # Class node.
    def __init__(self,ip,nxt=None):
        self.data=ip
        self.next=nxt


class linklist:                                     # Class linklist.
    def __init__(self):
        nd=node(None)
        self.head=nd
        self.tail=nd
        self.size=0

    def append(self,data):                          # Append is used to append new data node at the end of the link list.
        nd=node(data)
        if(self.size==0):
            self.head=nd
            self.tail=nd
        elif(self.size>0):
            self.tail.next=nd
            self.tail=nd
        self.size+=1
    
    def prepend(self,data):                         # Prepend is used to insert new data node at the starting of list.
        if(self.size==0):
            nd=node(data)
            self.head=nd
            self.tail=nd
        elif(self.size>0):
            nd=node(data,self.head)
            self.head=nd
        self.size+=1

    def insert(self,data,ind):                      # Insert is used to add new data node at given index.
        if(0<=ind<=self.size):
            if(ind==0):
                self.prepend(data)
            elif(ind==self.size):
                self.append(data)
            else:
                trvsl=self.head
                for i in range(ind-1):
                    trvsl=trvsl.next
                nd=node(data,trvsl.next)
                trvsl.next=nd
            self.size+=1
        else:
            raise Exception("Envalid Index")


    def size_cnt(self):                             # Count the size of the list.
        trvsl=self.head
        cnt=0
        while(trvsl!=None):
            trvsl=trvsl.next
            cnt+=1
        print(cnt)
    
    def len(self):                                  # Determine length directly from size var.
        print(self.size)
    
    def remove(self,ind):                           # Remove the element of the given index.
        if(0<=ind<self.size):
            if(ind==0):
                self.head=self.head.next
            else:
                trvsl=self.head
                for i in range(ind-1):
                    trvsl=trvsl.next
                trvsl.next=trvsl.next.next
            self.size-=1
        else:
            raise Exception("Envalid Index")
        
    def search(self,dataa):                          # Search the index of given value.
        cnt=0
        trvsl=self.head
        while(trvsl!= None):
            if(trvsl.data==dataa):
                return cnt
            trvsl=trvsl.next
            cnt+=1

    def rem_by_val(self,val):                       # Remove data node by value.
        idx=self.search(val)
        if(idx):
            self.remove(idx)   
        else:
            print("No such value in list")   


    def printlist(self):                            # Print function for link list display.
        if self.size==0:
            print("Linked List is empty")
            return
        else:
            trvsl = self.head
            output = ''
            while trvsl:
                output += str(trvsl.data)+' --> ' if trvsl.next else str(trvsl.data)
                trvsl = trvsl.next
            print(output)
                
