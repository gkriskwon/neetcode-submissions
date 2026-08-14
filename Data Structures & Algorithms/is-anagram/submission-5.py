from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        memo = defaultdict(int)
        for i in range(len(s)):
            memo[s[i]] += 1

        for c in t:
            if memo[c] == 0:
                return False
            memo[c] -= 1

        for v in memo.values():
            if v != 0:
                return False

        return True
        