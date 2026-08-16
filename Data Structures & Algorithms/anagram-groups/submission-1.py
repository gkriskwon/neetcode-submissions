class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Try to be better this time

        memo = defaultdict(list)
        
        for s in strs:
            sorted_s = ''.join(sorted(s))
            memo[sorted_s].append(s)

        return list(memo.values())