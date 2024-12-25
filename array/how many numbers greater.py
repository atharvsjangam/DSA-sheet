from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        num_map = {num: idx for idx, num in enumerate(sorted_nums)}
        return [num_map[num] for num in nums]

if __name__ == "__main__":
    nums = [8, 1, 2, 2, 3]
    solution = Solution()
    result = solution.smallerNumbersThanCurrent(nums)
    print("Numbers smaller than the current number:", result)
