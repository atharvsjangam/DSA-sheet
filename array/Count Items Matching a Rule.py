from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule_map = {'type': 0, 'color': 1, 'name': 2}
        rule_index = rule_map[ruleKey]
        return sum(1 for item in items if item[rule_index] == ruleValue)

if __name__ == "__main__":
    items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
    ruleKey = "color"
    ruleValue = "blue"
    solution = Solution()
    result = solution.countMatches(items, ruleKey, ruleValue)
    print("Number of items matching the rule:", result)
