from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(sentence.split()) for sentence in sentences)

if __name__ == "__main__":
    sentences = ["I love coding", "Python is awesome", "I enjoy learning new things"]
    solution = Solution()
    result = solution.mostWordsFound(sentences)
    print("Maximum number of words found in sentences:", result)
