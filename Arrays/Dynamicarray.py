import ctypes

#Creating a own array datatype name MeraList
class MeraList:
    def __init__(self):
        self.size=1 #to show the size of array
        self.n=0 # to show the number of element store in array
        self.A = self._create_array(self.size)
        
    def __len__(self):
        return self.n  
    def __str__(self):
        
        result=""
        for i in range(self.n):
            result = result + str(self.A[i])+','
        return '['+result[:-1]+']'  
    def __getitem__(self,index):
        if 0<= index < self.n:
            return self.A[index]
        else:
            return "Index Out of Range"

       
    def _create_array(self,capacity):
         return (capacity*ctypes.py_object)()
    
    def append(self,item):
        if self.n == self.size:
            self.__resize(self.size*2)

        self.A[self.n] = item   
        self.n = self.n+1
    
    def __resize(self,new_capacity):
        B  = self._create_array(new_capacity)
        self.size  = new_capacity

        for i in range(self.n):
            B[i] = self.A[i]

        self.A = B    

    def pop(self):
        if self.n == 0:
            return "Empty list"
        print(self.A[self.n-1])    
        self.n = self.n-1


        
l=MeraList()
print(len(l))
l.append(1)
l.append("hello")
l.append(2.4)
l.append(True)
l.append(7)
l.append(45)
l.pop()
l.pop()
l.pop()
print(l)


        
        