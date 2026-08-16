class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memo = defaultdict(int)
        for num in nums:
            memo[num] += 1

        count = list(memo.items())
        count.sort(key=lambda x: x[1])
        return [x[0] for x in count[-k:]]
