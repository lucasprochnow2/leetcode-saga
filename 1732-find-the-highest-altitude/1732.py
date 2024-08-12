"""1732. Find the Highest Altitude
https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
"""


class Solution:
    def largestAltitude(self, gain):
        prefixSum = result = 0

        for i in range(0, len(gain)):
            prefixSum += gain[i]
            result = max(prefixSum, result)

        return result


# gain = [-5,1,5,0,-7]  # 1
# gain = [-4,-3,-2,-1,4,3,2]  # 0
gain = [1, -2, 3]  # 2
result = Solution().largestAltitude(gain)
print('Result: ', result)
