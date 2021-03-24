class node:
    def __init__(self,d):
        self.data = d
        self.left = None
        self.right = None
    
    def insert(self, d):
        if d< self.data:
            if self.left == None: self.left = node(d)
            else: self.left.insert(d)
        elif d> self.data:
            if self.right == None: self.right = node(d)
            else: self.right.insert(d)
        else:
            return
        
    
def preorder(node):
    if not node:
        return []
    else:
        return [node.data] + preorder(node.left) + preorder(node.right)
    
a = [3,4,5,1,2]

root = node(3)
for i in range(1, len(a)):
    root.insert(a[i])

print(root)

print(preorder(root))