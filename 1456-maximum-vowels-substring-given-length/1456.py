"""1456. Maximum Number of Vowels in a Substring of Given Length
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        p1 = 0
        p2 = k - 1
        result = 0
        window_sum = 0

        while p2 <= len(s) - 1:
            if p1 == 0:
                for i in range(p1, p2 + 1):
                    if s[i] in vowels:
                        window_sum += 1
            else:
                prev_win_word = s[p1 - 1]
                curr_win_word = s[p2]

                if prev_win_word in vowels:  # Verifica se a letra que saiu da janela é uma vogal, se for decrementa o resultado
                    window_sum -= 1
                if curr_win_word in vowels:  # Verifica se a letra que entrou na janela é uma vogal, se for soma o resultado
                    window_sum += 1

            result = max(result, window_sum)

            print('--', s[p1], s[p2], '=', window_sum)
            p1 += 1
            p2 += 1

        return result


# s = "abciiidef"
# k = 3
# s = "aeiou"
# k = 2
s = "leetcode"
k = 3
result = Solution().maxVowels(s, k)
print('Result: ', result)
