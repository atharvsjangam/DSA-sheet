from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = sum(accounts[0])
        for i in accounts:
            m = max(m, sum(i))
        return m
