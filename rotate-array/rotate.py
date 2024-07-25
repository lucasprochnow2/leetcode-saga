# Essa foi a minha solução
class Solution:
    def rotate(self, nums, k: int) -> None:
        new_array = []

        for step in range(k):
            new_array.append(nums[-1])

            for key, num in enumerate(nums):
                if key != len(nums) - 1:
                    new_array.insert(key + 1, num)

            nums = list(new_array)
            new_array = []
            step += 1

        print(nums)


nums = [-1, -100, 3, 99]
Solution().rotate(nums, 2)


# Outra solução bem mais simples, mas não tão performática
class Solution:
    def rotate(self, nums, k: int) -> None:
        k = k % len(nums)

        for i in range(k):
            a = nums.pop()
            nums.insert(0, a)


# Solução do chatGPT
class Solution:
    def rotate(self, nums, k: int) -> None:
        n = len(nums)
        k = k % n  # In case k is larger than the array size

        # Helper function to reverse elements in the array
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Reverse the entire array
        reverse(0, n-1)
        # Reverse the first k elements
        reverse(0, k-1)
        # Reverse the remaining elements
        reverse(k, n-1)
