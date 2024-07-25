"""
    1768. Merge Strings Alternately: https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

    Return the merged string.
"""


class Solution:  # MINHA SOLUÇÃO
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedStr = ""
        counter = 0

        for key, letter in enumerate(word1):
            if len(word2) > key:
                mergedStr += letter + word2[key]
            else:
                mergedStr += letter
            counter += 1

        return mergedStr + word1[counter:] + word2[counter:]


word1 = "abcg"
word2 = "def"
mergedStr = Solution().mergeAlternately(word1, word2)
print('Result:', mergedStr)
