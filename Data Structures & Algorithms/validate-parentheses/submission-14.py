class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ref = {']':'[', ')': '(', '}': '{'}
        for c in s:
            if c in ref.values():
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if stack.pop() != ref[c]:
                    return False
        if len(stack) != 0:
            return False
        return True
