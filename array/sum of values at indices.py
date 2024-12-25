from typing import List

class Solution:
    def sumOfIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def count_set_bits(n: int) -> int:
            return bin(n).count('1')
        
        return sum(nums[i] for i in range(len(nums)) if count_set_bits(i) == k)

if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11]  # Example input
    k = 2  # Example number of set bits
    solution = Solution()
    result = solution.sumOfIndicesWithKSetBits(nums, k)
    print("Sum of values at indices with k set bits:", result)
