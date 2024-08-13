"""2215. Find the Difference of Two Arrays
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

Note that the integers in the lists may be returned in any order.
"""


# Minha solução
class Solution:
    def findDifference(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        result1 = []
        result2 = []

        for n in nums1:
            if n not in nums2:
                result1.append(n)

        for n in nums2:
            if n not in nums1:
                result2.append(n)

        return [result1, result2]


# Outra solução encontrada no leetcode usando o método difference do set
class Solution2:
    def findDifference(self, nums1, nums2):
        s1, s2 = set(nums1), set(nums2)
        return [s1.difference(s2), s2.difference(s1)]

# nums1 = [1,2,3]
# nums2 = [2,4,6]  # [[1,3],[4,6]]
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]  # [[3],[]]
result = Solution().findDifference(nums1, nums2)
print('Result:', result)
