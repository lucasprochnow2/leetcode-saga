"""392. Is Subsequence
https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

"""
Minha solução:

Cria dois ponteiros para acompanhar as letras das duas palavras;
Cria um loop e compara cada letra de cada palavra, se as letras são iguais,
move o ponteiro da primeira palavra pra frente, caso contrário só move o
ponteiro da segunda palavra.
Vai concatenando o resultado na variavel result e no final retorna
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t) == 0:
            return True
        if len(t) == 0:
            return False
        if len(s) == 0:
            return True

        p1 = 0
        p2 = 0
        result = ""

        while True:
            if s[p1] == t[p2]:
                result += s[p1]
                p1 += 1

            if p2 == len(t) - 1 or p1 == len(s):
                break

            p2 += 1

        return bool(s == result)


"""
Nesta solução faz o loop enquanto os ponteiro percorrem os dois arrays
No final compara se o ponteiro da primeira palavra é igual ao tamanho
da palavra.
"""
class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = tp = 0

        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1

        return sp == len(s)


s = ""
t = "ahbgdc"
result = Solution2().isSubsequence(s, t)
print('Result', result)
