from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]

if __name__ == "__main__":
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    solution = Solution()
    result = solution.kidsWithCandies(candies, extraCandies)
    print("Kids with the greatest number of candies:", result)
