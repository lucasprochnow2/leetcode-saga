class Solution {
  twoSum(numbers: number[], target: number) {
    let left = 1
    let right = numbers.length

    while (left < right) {
      const sum = numbers[left-1] + numbers[right-1]
      if (sum === target)
        return [left, right]

      if (sum > target) {
        right -= 1
        continue
      }

      left += 1
    }
  }
}

const numbers = [1,2,3,4]
const target = 3

// const numbers = [2,3,4]
// const target = 6

const res = new Solution().twoSum(numbers, target)

console.log('Result', res)
