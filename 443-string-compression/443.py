"""443. String Compression
https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.
"""

"""Minha solução

Para o leetcode aceitar a solução, é necessário alterar o input chars também. O que é bem esquisito...
Bom, o algoritmo cumpre a compressão conforme o solicitado.
"""
class Solution:
    def compress(self, chars):
        s = ""
        counter = 0

        for k, letter in enumerate(chars):
            if k == len(chars) - 1:
                counter += 1
                s += f'{letter}{counter}' if counter > 1 else letter
                counter = 0
                break

            nextLetter = chars[k + 1]
            if letter != nextLetter:
                counter += 1
                s += f'{letter}{counter}' if counter > 1 else letter
                counter = 0
                continue

            counter += 1

        chars = list(s)

        print(chars)
        return len(s)


class Solution2:
    def compress(self, chars):
        result = 0
        i = 0

        while i < len(chars):
            letter = chars[i]
            totalLetterCount = 0

            print('--', letter)

            # Conta a quantidade de ocorrencias da letra no array
            while i < len(chars) and chars[i] == letter:
                print('----', i)
                totalLetterCount += 1
                i += 1

            chars[result] = letter
            result += 1

            # Caso tenha mais de uma ocorrencia da string no array, adiciona a quantidade na var chars
            if totalLetterCount > 1:
                for c in str(totalLetterCount):
                    chars[result] = c
                    result += 1

        return result


# chars = ["a","a","b","b","c","c","c"]
# chars = ["a"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
result = Solution2().compress(chars);
print('Result:', result)
