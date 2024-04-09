class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.value = key

if __name__ == '__main__':
    print("Tree example")
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    
    root.left.left = Node(4)
    
    '''4 becomes left child of 2
        1
       / \
      2   3
     / \ / \
    4 None None None
   / \
   None None'''    
    
