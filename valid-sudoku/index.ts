class Solution {
  /**
   * @param {character[][]} board
   * @return {boolean}
   */
  isValidSudoku(board: string[][]): boolean {
    const lines = {}
    const columns = {}
    const squares = {}

    // Popular os valores das linhas do board no hash map
    for (let l in board) {
      const lineArr = board[l]
      lines[l] = []

      for (let k in lineArr) {
        if (lineArr[k] !== '.') {
          lines[l].push(lineArr[k])

          // Populate colunms
          if (columns[k] && columns[k].length)
            columns[k].push(lineArr[k])
          else
            columns[k] = [lineArr[k]]

          // Populate squares
          const squareIdx = Math.floor(parseInt(l) / 3) * 3 + Math.floor(parseInt(k) / 3)

          if (squares[squareIdx] && squares[squareIdx].length)
            squares[squareIdx].push(lineArr[k])
          else
            squares[squareIdx] = [lineArr[k]]
        }

      }
    }

    const kKeys = Object.keys(lines)
    for (let k in kKeys) {
      const key = kKeys[k]
      if (lines[key].length !== new Set(lines[key]).size)
        return false
    }

    const cKeys = Object.keys(columns)
    for (let c in cKeys) {
      const key = cKeys[c]
      if (columns[key].length !== new Set(columns[key]).size)
        return false
    }

    const sKeys = Object.keys(squares)
    for (let s in sKeys) {
      const key = sKeys[s]
      if (squares[key].length !== new Set(squares[key]).size)
        return false
    }

    return true
  }
}

const board = [["1","2",".",".","3",".",".",".","."],
              ["4",".",".","5",".",".",".",".","."],
              [".","9","8",".",".",".",".",".","3"],
              ["5",".",".",".","6",".",".",".","4"],
              [".",".",".","8",".","3",".",".","5"],
              ["7",".",".",".","2",".",".",".","6"],
              [".",".",".",".",".",".","2",".","."],
              [".",".",".","4","1","9",".",".","8"],
              [".",".",".",".","8",".",".","7","9"]]

// const board = [["1","2",".",".","3",".",".",".","."],
//               ["4",".",".","5",".",".",".",".","."],
//               [".","9","1",".",".",".",".",".","3"],
//               ["5",".",".",".","6",".",".",".","4"],
//               [".",".",".","8",".","3",".",".","5"],
//               ["7",".",".",".","2",".",".",".","6"],
//               [".",".",".",".",".",".","2",".","."],
//               [".",".",".","4","1","9",".",".","8"],
//               [".",".",".",".","8",".",".","7","9"]]

const solution = new Solution().isValidSudoku(board)

console.log('Result:', solution)
