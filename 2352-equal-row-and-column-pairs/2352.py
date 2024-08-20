"""2352. Equal Row and Column Pairs
https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
"""

from collections import defaultdict


# Solução que implementei e passou
class Solution:
    def equalPairs(self, grid):
        result = 0
        rowsOfColumns = [[] for i in range(0, len(grid))]

        # Constrói uma matriz com as colunas sendo as linhas
        for i in range(0, len(grid)):
            rowArr = grid[i]
            for k in range(0, len(rowArr)):
                rowsOfColumns[k].append(rowArr[k])

        # Itera no grid passando por cada linha comparando com cada coluna
        for i in range(0, len(grid)):
            row = grid[i]

            for k in range(0, len(rowsOfColumns)):
                if row == rowsOfColumns[k]:
                    result += 1

        return result


# Solução tirada do leetcode
class Solution2:
    def equalPairs(self, grid):
        rowFreq = defaultdict(lambda: 0)
        count = 0

        for row in grid:
            rowFreq[tuple(row)] += 1

        for col in zip(*grid):
            count += rowFreq[col]

        # O zip nesse caso serviu para transformar as colunas em linhas
        # https://www.geeksforgeeks.org/zip-in-python/
        print('---', list(zip(*grid)))

        return count


# grid = [[3,2,1],[1,7,6],[2,7,7]]
# - (Row 2, Column 1): [2,7,7]
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]

result = Solution2().equalPairs(grid)
print('Result: ', result)
