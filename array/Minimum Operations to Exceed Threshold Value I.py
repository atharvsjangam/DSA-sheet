from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        current_sum, left = 0, -1
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            while current_sum > target and left < right:
                current_sum -= nums[left + 1]
                left += 1
                
            if current_sum == target:
                return len(nums) - (right - left)
        
        return -1

if __name__ == "__main__":
    nums = [1, 1, 4, 2, 3]
    x = 5
    solution = Solution()
    result = solution.minOperations(nums, x)
    print("Minimum operations:", result)
