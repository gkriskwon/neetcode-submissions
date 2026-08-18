class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        left = 0
        max_freq = 0
        result = 0
        for right in range(len(s)):
            c = s[right]
            counts[c] += 1
            max_freq = max(max_freq, counts[c])


            if (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result

