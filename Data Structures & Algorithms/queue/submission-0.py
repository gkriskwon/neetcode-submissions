class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = Node(value)
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        new_node.prev = self.head
        new_node.next = self.head.next
        self.head.next.prev = new_node
        self.head.next = new_node

    def pop(self) -> int:
        if (self.isEmpty()):
            return -1
        result = self.tail.prev
        self.tail.prev = result.prev
        result.prev.next = self.tail
        
        r_value = result.value
        del result
        return r_value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        result = self.head.next
        self.head.next = result.next
        result.next.prev = self.head

        r_value = result.value
        del result
        return r_value
        
