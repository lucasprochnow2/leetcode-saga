"""345-reverse-vowels-string/
https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        keys = []
        myVowels = []

        # Este loop serve para salvar as vogais que aparecem na palavra e suas posições na palavra
        for key, letter in enumerate(s):
            if letter in vowels:
                keys.append(key)
                myVowels.append(letter)

        # Aqui faço um reverse nas vogais da palavra. Dessa forma eu já tenho a sequencia correta em que as vogais vão aparecer.
        reversedVowels = myVowels[::-1]
        result = list(s)
        for key, vowel in enumerate(reversedVowels):
            result[keys[key]] = vowel

        return "".join(result)


result = Solution().reverseVowels('leetcode')
print('Result:', result)
