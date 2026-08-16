class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(len(s))
            result.append('#')
            result.append(s)

        return ''.join(map(str, result))

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0
        while i < len(s):
            j = i

            # find shop
            while s[j] != '#':
                j += 1
            
            # read length
            length = int(s[i:j])

            # get index to read
            start = j + 1
            end = start + length
            result.append(s[start:end])

            # update next index to read
            i = end

        return result