"""283. Move Zeroes
https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

"""
A solução aqui usa um ponteiro que começa no final do array e fica monitorando quando
um número zero é movido para o final do array. Quando um número zero é adicionado
ao final do array, o ponteiro é decrementado para não passar pelos elementos do final
do array.
"""
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        p2 = len(nums) - 1

        while k < p2:
            num = nums[k]

            if num == 0:
                nums.append(num)
                nums.pop(k)
                p2 -= 1 # Decrementa o ponteiro do final do array, para evitar que o loop fique infinito
                continue

            k += 1

        print(nums)


nums = [0,1,0,3,12]
# nums = [0]
Solution().moveZeroes(nums)
