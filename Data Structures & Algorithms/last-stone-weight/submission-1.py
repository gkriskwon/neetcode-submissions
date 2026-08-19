class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-stone for stone in stones]
        heapq.heapify(s)
        while len(s) > 1:
            x = -heapq.heappop(s)
            y = -heapq.heappop(s)


            if x < y:
                heapq.heappush(s, -(y - x))
            elif x > y:
                # y is bigger because it is negative
                heapq.heappush(s, -(x - y))
            else:
                continue

        return -heapq.heappop(s) if len(s) else 0