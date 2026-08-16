class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memo = defaultdict(int)
        for num in nums:
            memo[num] += 1

        # k size min heap
        min_heap = []
        for num, count in memo.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap) 


        return [num for count, num in min_heap]