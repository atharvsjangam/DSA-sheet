from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count, left, right = 0, 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                count += (right - left)
                left += 1
            else:
                right -= 1
        return count

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    target = 5
    solution = Solution()
    result = solution.countPairs(nums, target)
    print("Number of pairs whose sum is less than target:", result)
