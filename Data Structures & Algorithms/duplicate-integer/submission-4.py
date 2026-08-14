class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memo: Dict[int, bool] = defaultdict(bool)
        for num in nums:
            if memo[num]:
                return True
            memo[num] = True
        return False