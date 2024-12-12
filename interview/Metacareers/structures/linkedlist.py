class MyLinkedList:

    def __init__(self):
        self.data = 0
        self.head = None
        self.count = 0

    def get(self, index: int) -> int:
        if index > self.count - 1 or index < 0:
            return -1

        node = self.head
        for i in range(self.count):
            node = node.link

        return node.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)

        if self.head == None:
            self.head = newNode
        else:
            newNode.link = self.head
            self.head = newNode
        self.count = self.count + 1

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)

        if self.head == None:
            self.head = newNode
        else:
            tmpNodeRef = self.head

            while tmpNodeRef.link != None:
                tmpNodeRef = tmpNodeRef.link

            tmpNodeRef.link = newNode
        self.count = self.count + 1

    # def addAtIndex(self, index: int, val: int) -> None:
    #     if index > self.count:
    #         return

    #     if index == self.count:
    #         self.addAtTail(val)

    #     newNode = new Node(val)
    #     count = 0
    #     curr = self.head
    #     while count <> index:
    #         curr.link = curr

    def print(self) -> None:
        tmpRef = self.head

        if self.count == 0:
            print('The list is empty')
        else:
            count = 0
            print(self.count, ' elements')
            while tmpRef != None:
                count = count + 1
                print(count, ':', tmpRef.val)
                tmpRef = tmpRef.link

    def deleteAtIndex(self, index: int) -> None:
        return

class Node:
    def __init__(self, val: int):
        self.val = val
        self.link = None

if __name__ == "__main__":
# Your MyLinkedList object will be instantiated and called as such:
    index = 0
    val = 0
    obj = MyLinkedList()
    # param_1 = obj.get(index)
    obj.addAtHead(3)
    obj.addAtHead(44)
    obj.print()
    obj.addAtTail(4)
    obj.addAtTail(67)
    obj.print()
    # obj.addAtIndex(index,val)
    # obj.deleteAtIndex(index)

