"""1207. Unique Number of Occurrences
https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
"""


# MInha solução
class Solution:
    def uniqueOccurrences(self, arr):
        myMap = {}

        for v in arr:
            if myMap.get(v) is None:
                myMap[v] = 1
            else:
                myMap[v] += 1

        result = []
        for key in myMap:
            if myMap[key] in result:
                return False
            else:
                result.append(myMap[key])

        return True


# Solução encontrada no leetcode
class Solution2:
    def uniqueOccurrences(self, arr):
        d = {}

        for v in arr:
            if d.get(v) is None:
                d[v] = 1
            else:
                d[v] += 1

        # Adiciona os valores do map num set e depois compara com o tamanho original
        # do map, se for diferente significa que algum número repetido foi removido
        # no set, indicando que o resultado é false
        s = set(d.values())
        if len(d.values()) != len(s):
            return False

        return True


# arr = [1,2,2,1,1,3]  # T
# arr = [1,2]  # F
arr = [-3,0,1,-3,1,1,1,-3,10,0]  # T
result = Solution2().uniqueOccurrences(arr)
print('Result:', result)
