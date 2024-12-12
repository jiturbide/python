from model import Node
    
class Queue:
    def __init__(self):
        self.tail = None
        self.head = None
        self.count = 0
        
    def push(self, data):
        node = Node(data)

        if self.tail == None:
            self.tail = node
            self.head = node
        else:
            node.next = self.tail
            self.tail = node
        self.count += 1
                
    def pop(self):
        if self.tail == None:
            raise Exception('Queue is empty')
        else:
            previous = None
            current = self.tail
            while current.next != None:
                previous = current
                current = current.next
            toPop = current
            self.head = previous
            if previous != None:
                previous.next = None
            else:
                self.tail = None
            
            self.count -= 1
            
            return toPop
        
    def peek(self):
        if self.head == None:
            return None
        else:
            return self.head.data   

    def items(self):
        items = []
        node = self.tail
        while node != None:
            items.append(node.data)
            node = node.next
        return items
        
    def size(self):
        return self.count
        
if __name__ == "__main__":
    
    q = Queue()
    q.push('A')
    q.push('B')
    q.push('C')
    print("peek:", q.peek())
    print("items:", q.size(), q.items())
    
    q.pop()
    print("peek:", q.peek())
    print("items:", q.size(), q.items())
    
    q.pop()
    q.pop()
    q.push('D')
    print("peek:", q.peek())
    print("items:", q.size(), q.items())

    # q.pop()
    