from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        # Use zip to combine the first and second halves of the list
        for i, j in zip(nums[:n], nums[n:]):
            res += [i, j]  # Add the pairs in the required interleaving order
        return res

# Example usage of the shuffle function
if __name__ == "__main__":
    # Initialize the Solution class
    sol = Solution()

    # Test case 1
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    result = sol.shuffle(nums, n)
    print(f"Shuffled result: {result}")  # Expected: [2, 3, 5, 4, 1, 7]

    # Test case 2
    nums = [1, 2, 3, 4, 5, 6]
    n = 3
    result = sol.shuffle(nums, n)
    print(f"Shuffled result: {result}")  # Expected: [1, 4, 2, 5, 3, 6]
