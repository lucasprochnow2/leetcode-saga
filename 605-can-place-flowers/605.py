"""605. Can Place Flowers
https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
"""


class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        totalPossibilities = 0

        for key, f in enumerate(flowerbed):
            if f == 0:
                prevPlace = (key == 0) or (flowerbed[key - 1] == 0)
                nextPlace = (key == len(flowerbed) - 1) or (flowerbed[key + 1] == 0)

                if prevPlace and nextPlace:
                    flowerbed[key] = 1
                    totalPossibilities += 1

                print(key, flowerbed)

        return totalPossibilities >= n


flowerbed = [0, 0, 1, 0, 1]
n = 1
result = Solution().canPlaceFlowers(flowerbed, n)
print('Result:', result)
