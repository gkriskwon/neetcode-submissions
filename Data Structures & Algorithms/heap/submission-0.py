class MinHeap:
    
    def __init__(self):
        # parent index // 2
        # left = index * 2
        # right = index * 2 + 1
        self.heap = [0]

    def push(self, val: int) -> None:
        # O(logN)
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)


    def pop(self) -> int:
        # O(logN)
        if len(self.heap) <= 1:
            return -1

        if len(self.heap) == 2:
            return self.heap.pop()

        result = self.heap[1]
        self.heap[1] = self.heap.pop() # 마지막 값을 루트로 이동
        self._bubble_down(1)
        return result

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        # nums 를 heap으로 교체 
        self.heap = [0] + nums
        # O(N)
        for i in range(len(self.heap) - 1 // 2, 0, -1):
            self._bubble_down(i)

    def _bubble_up(self, index):
        # parent is bigger? swap up
        while index > 1:
            parent = index // 2
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break


    def _bubble_down(self, index):
        # swap with the smaller child
        child = 2 * index
        # check left child exist
        while child < len(self.heap):
            # check right child exist and right child is smaller than the left
            if child + 1 < len(self.heap) and self.heap[child + 1] < self.heap[child]:
                child += 1
            
            # check current index < min(left child, right child) 
            if self.heap[index] <= self.heap[child]:
                break
            
            # swap
            self.heap[index], self.heap[child] = self.heap[child], self.heap[index]
            index = child
            child = 2 * index

        