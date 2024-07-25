class Solution1:
    def productExceptSelf(self, nums):
        result = []

        for key, num in enumerate(nums):
            total_left = 1
            total_right = 1

            if key == 0:
                for n in nums[1:len(nums)]:
                    total_right *= n
                result.append(total_right)
                continue

            if key == len(nums) - 1:
                for n in nums[0:len(nums)-1]:
                    total_left *= n
                result.append(total_left)
                continue

            # print(num, nums, nums[0:key], nums[key+1:len(nums)])
            for n in nums[0:key]:
                total_left *= n

            for n in nums[key+1:len(nums)]:
                total_right *= n

            result.append(total_left*total_right)

        return result


class Solution2:
    def productExceptSelf(self, nums):
        result = []

        for key, num in enumerate(nums):
            product = 1
            for key2, num2 in enumerate(nums):
                if key == key2:
                    continue

                product *= num2

            result.append(product)

        return result


# Solução das sugestões
class Solution3:
    def productExceptSelf(self, nums):
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        answer = [prefix[i] * suffix[i] for i in range(n)]

        return answer


nums = [1,2,3,4]
result = Solution3().productExceptSelf(nums)
print(result)

