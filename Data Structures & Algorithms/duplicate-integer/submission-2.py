class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memo: Dict[int, bool] = {}
        for num in nums:
            if num in memo.keys():
                return True
            memo[num] = True
        return False