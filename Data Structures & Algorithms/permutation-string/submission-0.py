class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        n1 = len(s1)
        n2 = len(s2)
        
        count1 = [0] * 26 # size of alphabet
        count2 = [0] * 26 # size of alphabet 

        for c in s1:
            count1[ord(c) - ord('a')] += 1

        for i in range(n1):
            count2[ord(s2[i]) - ord('a')] += 1

        if count1 == count2:
            return True

        left = 0

        for right in range(n1, n2):
            left = right - n1
            # add current char
            count2[ord(s2[right]) - ord('a')] += 1
            # remove the last char
            count2[ord(s2[left]) - ord('a')] -= 1

            if count1 == count2:
                return True

        return False
