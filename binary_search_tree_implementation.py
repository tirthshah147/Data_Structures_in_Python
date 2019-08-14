class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        root = self.root
        temp = root
        p=-1
        while root != None:
            temp = root
            if new_val < root.value:
                root = root.left
                p=0
            else:
                root = root.right
                p = 1
        if p==1:
            temp.right = Node(new_val)
        elif p==0:
            temp.left = Node(new_val)
            
        

    def search(self, find_val):
        root = self.root
        while root != None:
            if root.value == find_val:
                return True
            elif find_val < root.value:
                root = root.left
            else:
                root = root.right
        return False
            
    
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)