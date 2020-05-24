class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

def insert(r, val):
        #Enter you code here.
    if r is None:
        r = Node('')
        r.data = val
    elif val < r.data:
        if r.left is None:
            r.left = Node('')
            r.left.data = val
        else:
            insert(r.left, val)
    else:
        if r.right is None:
            r.right = Node('')
            r.right.data = val
        else:
            insert(r.right, val)
    return r

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
