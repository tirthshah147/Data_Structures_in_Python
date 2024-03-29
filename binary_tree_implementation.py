class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        temp = Node(None)
        temp.right = 0
        roots=[temp]
        root = self.root
        while root != 0:
            if root.right != None:
                roots.append(root)
            if root.value == find_val:
                return True
            root = root.left
            if root == None:
                root = roots.pop().right
        return False
        
                
                
        

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        temp = Node(None)
        temp.right = 0
        order=[]
        roots=[temp]
        root = self.root
        while root != 0:
            if root.right != None:
                roots.append(root)
            order.append(str(root.value))
            root = root.left
            if root == None:
                root = roots.pop().right
        
                

        
        return '-'.join(order)

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start != None:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        
        return False

    def preorder_print(self, start, traversal):
        if start != None:
            traversal =  traversal + str(start.value) + '-'
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()