class TreeNode:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.value = key
    
    def addNodes(self, list):
        for n in list:
            self.addNode(TreeNode(n))
        
    def addNode(self, node):
        if self.value > node.value:
            if self.left == None:
                self.left = node
            else:
                self.left.addNode(node)
        else:
            if self.right == None:
                self.right = node
            else:
                self.right.addNode(node)

    # Preorder traversal, NLR
    def preorder(self):
        self.process()
        if self.left != None:
            self.left.preorder()
        if self.right != None:
            self.right.preorder()

    # In order traversal, LNR
    def inorder(self):
        if self.left != None:
            self.left.inorder()
        self.process()
        if self.right != None:
            self.right.inorder()

    # Postorder traversal, LRN
    def postorder(self):
        if self.left != None:
            self.left.postorder()
        if self.right != None:
            self.right.postorder()
        self.process()
    
    def breadthSearch(self):
        queue = [self]
        while len(queue) > 0:
            processNode = queue.pop()
            processNode.process()
            if processNode.left != None:
                queue.insert(0, processNode.left)
            if processNode.right != None:
                queue.insert(0, processNode.right)
    
    def process(self):
        print(self.value,", ",end="")
    
    
    
if __name__ == '__main__':
    print("Tree example")
    
    root = TreeNode("F")
    root.addNodes(["B", "G", "A", "D", "I", "C", "E", "H"])
    
    root.preorder()
    print("")
    root.inorder()
    print("")
    root.postorder()
    print("")
    root.breadthSearch()