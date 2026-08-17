class Solution:
    def threeSum(self, numbers: List[int]) -> List[List[int]]:
        # Brute force O(N^3)
        # No need to check length due to constraints
        numbers.sort()
        n = len(numbers)
        result = []
        for i in range(n - 2):
            if numbers[i] > 0:
                break

            if i > 0 and numbers[i] == numbers[i - 1]:
                continue

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
                    result.append([numbers[i], numbers[start], numbers[end]])
                    start += 1
                    end -= 1
                    while start < end and numbers[start] == numbers[start - 1]:
                        start += 1
                    while start < end and numbers[end] == numbers[end + 1]:
                        end -= 1



        return result

        
