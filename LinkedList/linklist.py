from nodes import Node
class LinkList:
    def __init__(self):
        self.head =None
        self.n = 0
    def __len__(self):
        return self.n    
    
    def insert_head(self,value):
        #new Node
        new_node = Node(value)
        #Create Connection
        new_node.next = self.head
        #reassign Head
        self.head = new_node
        #Increment n
        self.n = self.n+1

    def __str__(self):
        curr = self.head
        result =""

        while curr != None:
            result = result+str(curr.data) + '->'
            curr = curr.next
        return result[:-2]   
    
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n = self.n+1
            return
        
        curr = self.head

        while curr.next != None:
            curr = curr.next

        curr.next = new_node   
        self.n = self.n+1 


    def insert_after(self,after,value):
        new_node = Node(value)
        
        curr = self.head
       
        while curr != None:
            
            if curr.data == after:
                break
            curr = curr.next

        if curr != None :
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n+1
        else:
            return "Item Not Found" 
           
    def clear(self):
        self.head =None
        self.n =0

    def delete_head(self):
         if self.head == None:
             return "Empty Linked List"
         self.head = self.head.next
         self.n = self.n - 1
    
    def pop(self):
        if self.head == None:
            return "Empty LL"
        curr = self.head
        if curr.next== None:
            return self.delete_head()
    
        while curr.next.next !=None:
            curr = curr.next
            

        # Now Curr is 2nd Last node of LL
        curr.next = None
        self.n = self.n -1     
    
    def remove(self,value):
        if self.head == None:
            return "Empty LL"
        if self.head.data == value:
            return self.delete_head()
        curr = self.head

        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next
        #Here we have 2 case
        # case1 :- Item not found
        if curr.next == None:
            return "Not Found"
        else:
            curr.next = curr.next.next
            self.n = self.n -1
        # case2 :- Item found   
    def search(self,item):
        curr = self.head
        pos = 0

        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos = pos + 1

        return "Item not found"  
    
    def __getitem__(self,index):
        curr = self.head
        pos = 0

        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos = pos+1
        
        return "IndexError"

l = LinkList()
l.insert_head(1)
l.insert_head(2)
l.insert_head(3)
l.insert_head(4)
l.insert_head(5)
print(l.search(5))
print(l[5 ])
 