class Solution:
    def threeSum(self, numbers: List[int]) -> List[List[int]]:
        # Brute force O(N^3)
        # No need to check length due to constraints
        numbers.sort()
        n = len(numbers)
        result = set()
        for i in range(n - 2):
            if numbers[i] > 0:
                break
            start = i + 1
            end = n - 1
            target = -numbers[i]

            while start < end:
                current_sum = numbers[start] + numbers[end]

                if current_sum < target:
                    start += 1
                elif current_sum > target:
                    end -= 1
                else:
                    result.add((numbers[i], numbers[start], numbers[end]))
                    start += 1
                    end -= 1

        return list(result)

        
