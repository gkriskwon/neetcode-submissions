class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            c = s[right]
            if c in memo and memo[c] >= left:
                left = memo[c] + 1

            memo[c] = right
            longest = max(longest, right - left + 1)

        return longest
            
            

