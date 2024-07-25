"""151. Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75


Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        str_to_arr = s.strip().split(" ")
        key_to_insert = 0

        while key_to_insert < len(str_to_arr):
            pos_to_insert = len(str_to_arr) - key_to_insert
            str_to_arr.insert(pos_to_insert, str_to_arr[0])

            str_to_arr.pop(0)
            key_to_insert += 1

        result = []
        for st in str_to_arr:
            if st != '':
                result.append(st)

        return " ".join(result)


class Solution2:
    def reverseWords(self, s: str) -> str:
        str_to_arr = s.strip().split(" ")[::-1]

        result = []
        for st in str_to_arr:
            if st != '':
                result.append(st)

        return " ".join(result)


class Solution3:
    def reverseWords(self, s: str) -> str:
        str_to_arr = s.strip().split(" ")

        result = ''
        for word in str_to_arr:
            if word == '':
                continue
            if result:
                result = f"{word} {result}"
            else:
                result = word

        return result


s = "the sky  is blue  "
result = Solution3().reverseWords(s)
print(result)
