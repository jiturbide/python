class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.value = key

class Tree:
    root = None
    def __init__(self):
        return

    def rootNode(self):
        return self.root

    def add(self, value):
        node = Node(value)
        if self.root == None:
            self.root = node
        else:
            self.addNode(self.root, value)

    def addNode(self, node: Node, value):
        if value > node.value:
            if node.right == None:
                node.right = Node(value)
            else:
                self.addNode(node.right, value)
        else:
            if node.left == None:
                node.left = Node(value)
            else:
                self.addNode(node.left, value)

    def preorder(self, node: Node):
        if node == None:
            return

        self.visit(node)
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node: Node):
        if node == None:
            return
        self.inorder(node.left)
        self.visit(node)
        self.inorder(node.right)

    def postorder(self, node: Node):
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        self.visit(node)

    def visit(self, node: Node):
        print(node.value, ", ", end="")

if __name__ == '__main__':
    print("Tree example")

    tree = Tree()
    tree.add('F')
    tree.add('B')
    tree.add('G')
    tree.add('A')
    tree.add('D')
    tree.add('I')
    tree.add('C')
    tree.add('E')
    tree.add('H')

    tree.preorder(tree.rootNode())
    print('')
    tree.inorder(tree.rootNode())
    print('')
    tree.postorder(tree.rootNode())

