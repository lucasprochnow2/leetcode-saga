"""1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""


# Minha solução: deu tudo errado, não consegui
class Solution:
    def longestOnes(self, nums, k: int) -> int:
        p1 = 0
        p2 = 0
        controlK = 0
        result = 0
        window_result = 0
        pLastZero = 0

        while p2 < len(nums):
            print('---', p2, ':', nums[p2])
            if nums[p2] == 0:
                controlK += 1
                pLastZero = p2

                if controlK <= k:
                    p2 += 1
                    window_result += 1
                else:
                    print('--------- reset', pLastZero)
                    p1 += 1
                    p2 = p1
                    controlK = 0
                    window_result = 0

            else:
                p2 += 1
                window_result += 1

            result = max(result, window_result)

        return result


# Link da solução com desenhor e tudo mais:
# https://leetcode.com/problems/max-consecutive-ones-iii/solutions/719833/python3-sliding-window-with-clear-example-explains-why-the-soln-works
class Solution2:
    def longestOnes(self, nums, k: int) -> int:
        left = right = 0

        for right in range(len(nums)):
            # if we encounter a 0 the we decrement K
            if nums[right] == 0:
                k -= 1
            # else no impact to K

            # if K < 0 then we need to move the left part of the window forward
            # to try and remove the extra 0's
            if k < 0:
                # if the left one was zero then we adjust K
                if nums[left] == 0:
                    k += 1
                # regardless of whether we had a 1 or a 0 we can move left side by 1
                # if we keep seeing 1's the window still keeps moving as-is
                left += 1

        return right - left + 1



# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
# nums = [0,0,0,1]
# k = 4
result = Solution2().longestOnes(nums, k)
print('Result: ', result)
