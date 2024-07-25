"""1071. Greatest Common Divisor of Strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75

O problema 1071 do LeetCode, "Greatest Common Divisor of Strings" (Maior Divisor Comum de Strings), pede que você encontre a maior string possível que seja um divisor comum de duas strings dadas, str1 e str2.

Uma string X é um divisor de Y se Y pode ser construída ao concatenar múltiplas cópias de X. Por exemplo, para as strings "ABCABC" e "ABC", "ABC" é um divisor comum.

Seu objetivo é encontrar a maior string G que seja um divisor comum de str1 e str2. Se não houver tal string, o resultado deve ser uma string vazia.
"""


# https://leetcode.com/problems/greatest-common-divisor-of-strings/solutions/5315862/python-solution-with-explaination-beginner-freindly
# Explicação da solução, não consegui implementar.
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if concatenated strings are equal or not, if not return ""
        if str1 + str2 != str2 + str1:
            return ""
        # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)
        from math import gcd
        return str1[:gcd(len(str1), len(str2))]


str1 = "ABABAB"
str2 = "ABAB"
result = Solution().gcdOfStrings(str1, str2)
print('Result:', result)
