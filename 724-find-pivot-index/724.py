"""724. Find Pivot Index
https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan-v2&envId=leetcode-75

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""


"""
Minha ideia principal com esta solução foi somar todo o array antes de tudo.
Com esta soma, em cada iteração do array basta eu diminuir os valores
para obter o valor da soma da direita, e somar os valores para obter o left.
"""
class Solution:
    def pivotIndex(self, nums):
        result = -1
        right = sum(nums)
        left = 0

        for i in range(0, len(nums)):
            left += nums[i - 1] if i > 0 else 0
            right -= nums[i]

            if left == right:
                result = max(i, result) if result == -1 else min(i, result)

        return result

# nums = [1,7,3,6,5,6]  # 3
# nums = [1,2,3]  # -1
nums = [2,1,-1]  # 0
result = Solution().pivotIndex(nums)
print('Result: ', result)
