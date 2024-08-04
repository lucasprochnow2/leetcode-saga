"""11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

# Link com a explicação da solução: https://leetcode.com/problems/container-with-most-water/solutions/5139915/video-simple-two-pointer-solution/
class Solution:
    def maxArea(self, height) -> int:
        result = 0
        p1 = 0
        p2 = len(height) - 1

        while p1 < p2:
            xTotal = p2 - p1
            yTotal = min(height[p1], height[p2])
            area = xTotal * yTotal

            if area > result:
                result = area

            # Verifica qual é a maior barra.
            # Move o ponteiro que possui o menor valor
            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1

        return result


height = [1,8,6,2,5,4,8,3,7] # 49
# height = [1,1]
# height = [2,3,10,5,7,8,9] # 36
# height = [1,3,2,5,25,24,5] # 24

result = Solution().maxArea(height)
print('Result: ', result)
