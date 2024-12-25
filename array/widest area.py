from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        return max(points[i][0] - points[i - 1][0] for i in range(1, len(points)))

if __name__ == "__main__":
    points = [[8, 7], [9, 9], [7, 4], [9, 7]]
    solution = Solution()
    result = solution.maxWidthOfVerticalArea(points)
    print("Widest Vertical Area:", result)
