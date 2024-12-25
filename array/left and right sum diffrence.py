from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = 0
        right_sum = sum(nums)
        result = []
        
        for num in nums:
            right_sum -= num
            result.append(abs(left_sum - right_sum))
            left_sum += num
            
        return result

if __name__ == "__main__":
    nums = [10, 4, 8, 3]
    solution = Solution()
    result = solution.leftRightDifference(nums)
    print("Left and Right Sum Differences:", result)
