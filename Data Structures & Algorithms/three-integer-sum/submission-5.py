class Solution:
    def threeSum(self, numbers: List[int]) -> List[List[int]]:
        # Brute force O(N^3)
        # No need to check length due to constraints
        new_numbers = sorted(numbers)
        n = len(new_numbers)
        result = set()
        for i in range(n - 2):
            
            start = i + 1
            end = n - 1
            target = -new_numbers[i]

            while start < end:
                current_sum = new_numbers[start] + new_numbers[end]

                if current_sum < target:
                    start += 1
                elif current_sum > target:
                    end -= 1
                else:
                    result.add((new_numbers[i], new_numbers[start], new_numbers[end]))
                    start += 1
                    end -= 1

            # became two pointer approach

        return list(result)

        
