import math

"""374. Guess Number Higher or Lower
https://leetcode.com/problems/guess-number-higher-or-lower/description/?envType=study-plan-v2&envId=leetcode-75

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


# Binary search
class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 1
        hi = n

        while lo <= hi:
            middle = math.floor((lo + hi) / 2)
            theGuess = guess(middle)

            if theGuess == 0:
                return middle

            if theGuess == -1:
                hi = middle - 1
            else:
                lo = middle + 1


def guess(n):
    correct_guess = 4

    if n == correct_guess:
        return 0

    if n < correct_guess:
        return 1

    return -1


n = 4
result = Solution().guessNumber(n)
print(result)
