class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(c.lower() for c in s if c.isalnum())

        start = 0
        end = len(clean_s) - 1
        while start <= end:
            if clean_s[start] != clean_s[end]:
                return False
            start += 1
            end -= 1

        return True