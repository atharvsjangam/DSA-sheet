from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        
        # Loop through each word in the list and check if 'x' is in the word
        for i in range(len(words)):
            if x in words[i]:
                res.append(i)  # Append the index of the word if 'x' is found
        
        return res

# Example usage:
if __name__ == "__main__":
    # Create an instance of Solution class
    sol = Solution()
    
    # Test case 1
    words = ["apple", "banana", "grape", "orange", "pineapple"]
    x = "apple"
    result = sol.findWordsContaining(words, x)
    print(f"Words containing '{x}': {result}")  # Expected: [0, 4]

    # Test case 2
    words = ["cat", "dog", "bat", "rat", "cow"]
    x = "at"
    result = sol.findWordsContaining(words, x)
    print(f"Words containing '{x}': {result}")  # Expected: [0, 2, 3]
