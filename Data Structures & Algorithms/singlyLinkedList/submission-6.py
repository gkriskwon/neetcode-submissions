class LinkedList:
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = self.Node(-1)  # dummy node
        self.tail = self.head
        self.length = 0
    
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        
        c = self.head
        while index >= 0:
            c = c.next
            index -= 1

        return c.val

    def insertHead(self, val: int) -> None:
        new_node = self.Node(val, self.head.next)
        if self.tail == self.head:
            self.tail = new_node
        self.head.next = new_node
        self.length += 1
        # print(self.getValues())

    def insertTail(self, val: int) -> None:
        new_node = self.Node(val)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        # print(self.getValues())

    def remove(self, index: int) -> bool:
        if index >= self.length:
            return False
        c = self.head
        while index > 0:
            c = c.next
            index -= 1
        to_remove = c.next
        c.next = c.next.next
        if self.tail is to_remove:
            self.tail = c
        del to_remove
        self.length -= 1
        # print(self.getValues())

        return True
            
    def getValues(self) -> List[int]:
        result = []
        c = self.head.next
        # print(self.length)
        while c:
            # print(c.val)
            result.append(c.val)
            c = c.next

        return result
 
