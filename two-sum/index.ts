class Solution {
  twoSum(nums: number[], target: number): number[] {
    const hash = new Map();

    for (let i = 0; i < nums.length; i++) {
      const diff = target - nums[i]

      if (hash.has(diff))
        return [hash.get(diff), i]

      hash.set(nums[i], i)
    }

    return [];
  }
}

const solution = new Solution()

const nums = [3,4,5,6]
const target = 7
// const nums = [4,5,6]
// const target = 10
// const nums = [5,5]
// const target = 10

console.log('Result: ', solution.twoSum(nums, target))
