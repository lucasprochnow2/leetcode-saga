"""334. Increasing Triplet Subsequence
https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
"""

"""
A solução proposta é manter track dos dois menores valores do array e conforme percorre
o array, caso o valor atual não seja menor que estes valores, significa que ele é maior
e satisfaz a ocorrencia: num1 < num2 < num3
"""
class Solution:
    def increasingTriplet(self, nums) -> bool:
        if len(nums) < 3:
            return False

        first = float('inf') # Infinito - usado para que qualquer n do loop seja menor
        second = float('inf')
        print(first, second)

        for n in nums:
            if n <= first:
                first = n  # smallest so far
            elif n <= second:
                second = n  # second smallest
            else:
                print(first, second, n)
                return True  # found a triplet

        return False


# nums = [1,2,3,4,5]
# nums = [20,100,10,12,5,13]
nums = [2,1,5,0,4,6]
# nums = [5,4,3,2,1]
result = Solution().increasingTriplet(nums)
print('Result:', result)
