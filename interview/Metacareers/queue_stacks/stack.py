from model import Node
    
class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
        
    def push(self, data):
        node = Node(data)

        if self.top == None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.count += 1
                
    def pop(self):
        if self.top == None:
            raise Exception('Stack is empty')
        else:
            toPop = self.top
            self.top = self.top.next
            self.count -= 1

            return toPop
        
    def peek(self):
        if self.top == None:
            return None
        else:
            return self.top.data   

    def items(self):
        items = []
        node = self.top
        while node != None:
            items.append(node.data)
            node = node.next
        return items
        
    def size(self):
        return self.count
        
if __name__ == "__main__":
    
    stack = Stack()
    stack.push('A')
    stack.push('B')
    stack.push('C')
    print("peek:", stack.peek())
    print("items:", stack.size(), stack.items())
    
    stack.pop()
    print("peek:", stack.peek())
    print("items:", stack.size(), stack.items())
    
    stack.pop()
    stack.pop()
    print("peek:", stack.peek())
    print("items:", stack.size(), stack.items())
    