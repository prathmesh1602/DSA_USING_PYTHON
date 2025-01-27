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
        else:
            return "Item Not Found" 
           




    

l = LinkList()
l.insert_head(1)
l.insert_head(2)
l.insert_head(3)
l.insert_head(4)
l.insert_head(5)

print(l)   
l.insert_after(4,7)
print(l.insert_after(21,5))
print(l)
