from typing import List

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(1 for h in hours if h >= target)

if __name__ == "__main__":
    hours = [8, 5, 6, 10, 7]
    target = 6
    solution = Solution()
    result = solution.numberOfEmployeesWhoMetTarget(hours, target)
    print("Number of employees who met the target:", result)
