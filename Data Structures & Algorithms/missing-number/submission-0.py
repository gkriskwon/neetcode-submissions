class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        size = len(nums)
        for i in range(size):
            result ^= i
            result ^= nums[i]

        return result ^ (size)