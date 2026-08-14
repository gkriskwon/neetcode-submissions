class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memo: set[int] = set()
        for num in nums:
            if num in memo:
                return True

            memo.add(num)
        return False