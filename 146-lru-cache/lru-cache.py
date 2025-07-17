class Node:
    def __init__(self,key,value):
        self.key=key
        self.val=value
        self.prev=self.next=None

class LRUCache(object):

    def __init__(self, capacity):
        self.d={}
        self.cap=capacity
        
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next,self.right.prev=self.right,self.left
    
    def remove(self,node):
        prev,nxt=node.prev,node.next
        prev.next,nxt.prev=nxt,prev
    
    def insert(self,node):
        prev,nxt=self.right.prev,self.right
        prev.next=nxt.prev=node
        node.next,node.prev=nxt,prev


    def get(self, key):
        if key in self.d:
            self.remove(self.d[key])
            self.insert(self.d[key])
            return self.d[key].val
        return -1
        

    def put(self, key, value):
        if key in self.d:
            self.remove(self.d[key])
        self.d[key]=Node(key,value)
        self.insert(self.d[key])
        
        if len(self.d)>self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.d[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)