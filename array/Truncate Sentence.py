class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        return ' '.join(words[:k])

if __name__ == "__main__":
    s = "Hello how are you Contestant"
    k = 4
    solution = Solution()
    result = solution.truncateSentence(s, k)
    print("Truncated sentence:", result)
