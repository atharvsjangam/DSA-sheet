from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total_sum = 0
        n = len(arr)
        
        # Iterate over all possible odd lengths
        for length in range(1, n + 1, 2):  # step by 2 to consider only odd lengths
            for start in range(n - length + 1):
                total_sum += sum(arr[start:start + length])
        
        return total_sum

# Example usage
if __name__ == "__main__":
    arr = [1, 4, 2, 5, 3]
    solution = Solution()
    result = solution.sumOddLengthSubarrays(arr)
    print("Sum of all odd-length subarrays:", result)
