"""643. Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
"""


# Primeira solução: não eficiente por conta do loop dentro do while para somar
class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        p1 = 0
        p2 = k - 1
        result = None

        while p2 <= len(nums) - 1:
            theSum = 0
            for i in range(p1, p2 + 1):
                theSum += nums[i]

            theAvg = theSum / k
            if result is None:
                result = theAvg
            elif theAvg > result:
                result = theAvg

            p1 += 1
            p2 += 1

        return result


"""
Para esta solução, me baseei nesta explicação de sliding window: https://www.geeksforgeeks.org/window-sliding-technique/
Não há necessidade de fazer um loop para somar os valores da window toda vez, apenas da primeira.
Nas windows seguintes, basta subtrair o valor que saiu da janela e somar o valor que entrou.
"""
class Solution2:
    def findMaxAverage(self, nums, k: int) -> float:
        p1 = 0
        p2 = k - 1
        result = -float('inf')
        window_sum = 0

        while p2 <= len(nums) - 1:
            if p1 == 0:
                for i in range(p1, p2 + 1):
                    window_sum += nums[i]
            else:
                window_sum += -nums[p1-1] + nums[p2]

            theAvg = window_sum / k
            if theAvg > result:
                result = theAvg

            p1 += 1
            p2 += 1

        return result


# nums = [1,12,-5,-6,50,3]
# k = 4
nums = [5]
k = 1
# nums = [-1]
# k = 1
result = Solution2().findMaxAverage(nums, k)
print('Result: ', result)
