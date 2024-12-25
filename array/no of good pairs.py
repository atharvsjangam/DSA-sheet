from typing import List


class Solution:
    # Method to count good pairs
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Dictionary to store the count of occurrences
        repeat = {}
        num = 0  # Initialize the number of good pairs

        # Iterate through the list
        for v in nums:
            # If the number has been seen before
            if v in repeat:
                # Add the count of existing pairs
                num += repeat[v]
                # Increment the count for this number
                repeat[v] += 1
            # If the number has not been seen before
            else:
                repeat[v] = 1
