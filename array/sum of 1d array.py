from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    solution = Solution()
    result = solution.runningSum(nums)
    print("Running sum of 1D array:", result)
