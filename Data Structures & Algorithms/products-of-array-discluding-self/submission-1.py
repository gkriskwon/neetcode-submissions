class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]

        for i in range(1, n):
            prefix[i] = nums[i] * prefix[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i] * suffix[i + 1]

        # prefix and suffix ready
        # print(prefix)
        # print(suffix)
        result = [0] * n
        result[0] = suffix[1]
        result[-1] = prefix[-2]
        for i in range(1, n - 1):
            result[i] = prefix[i - 1] * suffix[i + 1]

        return result

        