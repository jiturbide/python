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
        print()
                
    def __traverse(self, node: Node):
        if node == None:
            return
        self.__traverse(node.left)
        self.visit(node)
        self.__traverse(node.right)
        
    def visit(self, node: Node):
        print(node.value, end=", ")
        
    def commonAncestor(self, a, b):
        common = None
        
        # get ancestors of a
        lista = [None]
        self.ancestors(self.root, a, lista)
        print('Ancestors of ',a, lista)
        
        # get ancestors of b
        listb = [None]
        self.ancestors(self.root, b, listb)
        print('Ancestors of ',b, listb)
        
        # extract common ancestor
        for i in reversed(range(len(lista))):
            for j in reversed(range(len(listb))):
                if lista[i] == listb[j]:
                    common = lista[i]
                    break
            if common != None:
                break    
                
        print('------> common:', common)
        return common
        
    def ancestors(self, node: Node, value, listAncestors):
        if node == None:
            return False
        if node.value == value:
            return True
        listAncestors.append(node.value)
        foundL = self.ancestors(node.left, value, listAncestors)
        foundR = self.ancestors(node.right, value, listAncestors)
        
        if foundL == False and foundR == False:
            listAncestors.pop()
            return False
        
         
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
    tree.add(11)
    tree.add(17)
    
    tree.traverse()

    result = tree.commonAncestor(8,15)
    print("result:", 8, 15, result)    
    
    result = tree.commonAncestor(11,17)
    print("result:", 11, 17, result)    
    
    result = tree.commonAncestor(9,9)
    print("result:", 11, 17, result)    
    