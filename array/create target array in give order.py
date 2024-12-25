from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for num, idx in zip(nums, index):
            target.insert(idx, num)
        return target

if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]
    solution = Solution()
    result = solution.createTargetArray(nums, index)
    print("Target array:", result)
