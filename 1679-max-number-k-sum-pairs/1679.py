"""1679. Max Number of K-Sum Pairs
https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
"""


# Minha primeira tentativa.. Não deu certo.
class Solution:
    def maxOperations(self, nums, k: int) -> int:
        operations = 0
        p1 = 0
        p2 = len(nums) - 1

        while p1 < p2:
            if nums[p1] > k:
                p1 += 1
                p2 -= 1
                continue

            print('---', p1, p2)
            print('------', nums[p1], nums[p2])
            # nums.pop(p1)
            # nums.delete(p2)

            operations += 1

            if nums[p1] + nums[p2] == k:
                break

            p1 += 1
            p2 -= 1

        return operations


# Solução descrita aqui: https://leetcode.com/problems/max-number-of-k-sum-pairs/solutions/4363338/python-two-pointer-well-explain-solution-quick-and-still-mantain-o-1-space-complexity
class Solution2:
    def maxOperations(self, nums, k: int) -> int:
        nums.sort()
        p1 = 0
        p2 = len(nums) - 1
        operations = 0

        while p1 < p2:
            theSum = nums[p1] + nums[p2]

            if theSum == k:
                p1 += 1
                p2 -= 1
                operations += 1
            elif theSum < k:
                p1 += 1
            else:
                p2 -= 1

        return operations


# nums = [1,2,3,4]
# k = 5
# nums = [3,1,3,4,3]
# k = 6
nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k = 2
result = Solution2().maxOperations(nums, k)
print('Result: ', result)
