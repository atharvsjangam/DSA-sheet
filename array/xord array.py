from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded = [first]
        for num in encoded:
            decoded.append(decoded[-1] ^ num)
        return decoded

if __name__ == "__main__":
    encoded = [1, 2, 3]
    first = 1
    solution = Solution()
    result = solution.decode(encoded, first)
    print("Decoded array:", result)
