class Solution:
    def countBits(self, n: int) -> List[int]:
        memo = [0] * (n + 1)

        for i in range(1, n + 1):
            memo[i] = memo[ i // 2] + (i % 2) 

        return memo

