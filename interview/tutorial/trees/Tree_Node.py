class Node:
    
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
class Tree:
    def __init__(self):
        self.root = None
       
    def add(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.__add(self.root, value)
       
    def __add(self, node: Node, value):      
        if value > node.value:
            if node.right != None:
                self.__add(node.right, value)
            else:
                node.right = Node(value)
        else:
            if node.left != None:
                self.__add(node.left, value)
            else:
                node.left = Node(value)
    
    def traverse(self):
        self.__traverse(self.root)
                
    def __traverse(self, node: Node):
        if node == None:
            return
        self.__traverse(node.left)
        self.visit(node)
        self.__traverse(node.right)
        
    def visit(self, node: Node):
        print(node.value)
        
        
if __name__ == "__main__":
    tree = Tree()
    tree.add(9)
    tree.add(8)
    tree.add(12)
    tree.add(5)
    tree.add(7)
    tree.add(2)
    tree.add(15)
    tree.add(10)
    
    tree.traverse()
    