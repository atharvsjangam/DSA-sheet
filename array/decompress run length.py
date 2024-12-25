from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums), 2):
            result.extend([nums[i]] * nums[i + 1])
        return result

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    solution = Solution()
    result = solution.decompressRLElist(nums)
    print("Decompressed list:", result)
