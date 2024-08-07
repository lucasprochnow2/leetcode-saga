"""1493. Longest Subarray of 1's After Deleting One Element
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
"""


# Minha solução
class Solution:
    def longestSubarray(self, nums) -> int:
        p1 = p2 = pLastZero = window_result = result = 0
        hasZeros = False
        k = 1

        while p2 < len(nums):
            print('---', f'{p2}:{nums[p2]}')
            if nums[p2] == 0:
                k -= 1
                hasZeros = True

                if k < 0:
                    k = 1
                    p1 = p2 = pLastZero + 1
                    window_result = 0
                else:
                    pLastZero = p2
                    p2 += 1

            else:
                window_result += 1
                p2 += 1

            result = max(result, window_result)

        if not hasZeros:
            result -= 1

        return result


# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/solutions/5528894/very-concise-and-intuitive-solution/?envType=study-plan-v2&envId=leetcode-75
class Solution2:
    def longestSubarray(self, nums) -> int:
        if sum(nums) == len(nums):
            return len(nums) - 1

        L, R = 0, 0
        max_len = 0
        zero_index = -1

        while R < len(nums):
            if nums[R] == 0:
                if zero_index != -1:
                    L = zero_index + 1
                zero_index = R
            max_len = max(max_len, R - L)
            R += 1

        return max_len


# nums = [1,1,0,1] # 3
# nums = [0,1,1,1,0,1,1,0,1] # 5
nums = [1,1,1] # 2
result = Solution().longestSubarray(nums)
print('Result:', result)
