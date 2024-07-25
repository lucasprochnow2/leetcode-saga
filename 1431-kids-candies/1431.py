"""1431. Kids With the Greatest Number of Candies
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75

There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
"""


"""
Minha ideia foi passar pelo array de candies e salvar em uma variável qual
é o maior valor de doces do array.

O próximo loop serve para pegar o resultado somando os doces das crianças
com os doces extras e verificando se ultrapassa o maior valor que salvamos
do loop anterior.
"""


class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        greatestNumber = 0
        result = []

        for x in candies:
            if x > greatestNumber:
                greatestNumber = x

        for x in candies:
            total = x + extraCandies
            if total >= greatestNumber:
                result.append(True)
            else:
                result.append(False)

        return result


candies = [12, 1, 12]
extraCandies = 10
result = Solution().kidsWithCandies(candies, extraCandies)
print('Result:', result)


# Outra solução usando a função `max`
class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        result_lst = []
        max_num = max(candies)

        for num in candies:
            result_lst.append(num + extraCandies >= max_num)

        return result_lst
