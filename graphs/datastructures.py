#Graph

class GraphNode:
    def __init__(self,x):
        self.value = x
        self.visited = False

n0 = GraphNode(0)
n1 = GraphNode(1)
n2 = GraphNode(2)
n3 = GraphNode(3)
n4 = GraphNode(4)
n5 = GraphNode(5)

graph = {n0:[n1, n4, n5], n1:[n3, n4], n2:[n1], n3:[n2, n4], n4:[], n5:[]}
 
def dfs(root):
    if root==None:
        return 
    print(root.value)
    root.visited = True
    for node in graph[root]:
        if node.visited == False:
            dfs(node)

def bfs(root):
    queue = []
    root.visited = True
    queue.append(root)
    while(queue!=[]):
        r = queue.pop(0)
        print(r.value)
        for node in graph[r]:
            if node.visited==False:
                node.visited = True
                queue.append(node)


#BST
class Node:
    def __init__(self,x):
        self.right = None
        self.left = None
        self.data = x
        
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
        
    def add(self,x):
        node = Node(x)
        if self.root==None:
            self.root = node
            return
            
        a = b = self.root
        
        while(a!=None):
            b = a
            if (x <= a.data):
                a = a.left
            else:
                a = a.right
                
        if x <= b.data:
            b.left = node
            
        else:
            b.right = node
            
    def delete(self, x):
        a = b = self.root
        while(a!=None and a.data!=x):
            b = a
            if x <= a.data:
                a = a.left
            else:
                a = a.right
                
                
        if a==None:
            print("Element Not Found")
            return
            
        if a.left!=None and a.right==None:
            
            if a==self.root:
                self.root = a.left
                
            else:
                if b.left == a:
                    b.left = a.left
                    
                else:
                    b.right = a.left
                    
        elif a.left==None and a.right!=None:
            if a==self.root:
                self.root = a.right
                
            else:
                if b.left == a:
                    b.left = a.right
                    
                else:
                    b.right = a.right
                    
        elif a.left==None and a.right==None:
            if a==self.root:
                self.root = None
                
            else:
                if b.left == a:
                    b.left = None
                    
                else:
                    b.right = None
                    
                    
        else:
            c = a.right
            
            while(c.left!=None):
                c = c.left
                
            c.left = a.left
            
            if a==self.root:
                self.root = a.right
                
            else:
                if b.left == a:
                    b.left = a.right
                    
                else:
                    b.right = a.right
            
      

B1 = BinaryTree()
for data in [7, 96, 125, 8, 100, 15, -2, -21]:
    B1.add(data)

def inorder(root):
    if root!=None:
        
            
        inorder(root.left)
        print(root.data)
        inorder(root.right)




#LINKED LIST

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#         self.prev = None
        
        
        
    def print(self):
        print("{}".format(self.data))
        
        
        
class SinglyLinkedList:
    def __init__(self):
        self.top = None
        self.end = None
        
    def add(self,data):
        node = Node(data)
        
        if self.top == self.end == None:
            self.top = self.end = node
        else:
            self.end.next = node
            self.end = node

ll = SinglyLinkedList()
for i in ['A','B','C','D','E']:
    ll.add(i)

ll.print()

