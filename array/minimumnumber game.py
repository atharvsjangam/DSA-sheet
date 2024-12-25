from typing import List

class Solution:
    def minNumberGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            new_nums = []
            for i in range(0, len(nums) - 1, 2):
                new_nums.append(min(nums[i], nums[i + 1]))
            if len(nums) % 2 == 1:
                new_nums.append(nums[-1])
            nums = new_nums
        return nums[0]

if __name__ == "__main__":
    nums = [2, 1, 3, 4, 5, 6]
    solution = Solution()
    result = solution.minNumberGame(nums)
    print("Minimum number in the game:", result)
