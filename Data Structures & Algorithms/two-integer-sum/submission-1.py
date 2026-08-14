class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo: Dict[int, int] = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in memo:
                return [memo[diff], i]
            memo[num] = i

        