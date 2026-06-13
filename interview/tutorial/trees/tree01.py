# https://en.wikipedia.org/wiki/Tree_traversal


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

    def search(self, value):
        return self.searchNode(self.root, value)

    def searchNode(self, node: Node, value):
        if node == None:
            return None
        if node.value == value:
            return node
        if value < node.value:
            return self.searchNode(node.left, value)
        return self.searchNode(node.right, value)

    def breadthFirst(self):
        self.breadthFirstNode(self.root)

    def breadthFirstNode(self, initialNode: Node):
        if initialNode == None:
            return
        queue = []
        queue.append(initialNode)

        while len(queue) > 0:
            node = queue.pop(0)
            self.visit(node)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)

    def visit(self, node: Node):
        print(node.value, ", ", end="")

if __name__ == '__main__':
    print("Tree example")

#      F
#     / \
#    B   G
#   / \   \
#  A   D    I
#     / \    \
#    C   E    H
#

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
    print()
    node = tree.search('E')
    if node != None:
        print("Node ", node.value, " found")
    else:
        print("Node not found")

    tree.breadthFirst()
    print()