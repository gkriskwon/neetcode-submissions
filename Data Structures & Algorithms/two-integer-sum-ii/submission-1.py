class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        memo = {} # value seen: 1-indexed 
        result = []
        for i, number in enumerate(numbers):
            diff = target - number
            if diff in memo:
                return [memo[diff], i + 1]
            memo[number] = i + 1
            

        return result

