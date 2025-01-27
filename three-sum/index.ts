class Solution {
  /**
   * @param {number[]} nums
   * @return {number[][]}
   */
  threeSum(nums: number[]): number[][] {
    nums.sort((a, b) => a-b)
    const res = []

    for (let i in nums) {
      if (parseInt(i) > 0 && nums[i] === nums[parseInt(i) - 1]) continue

      let pLeft = parseInt(i) + 1
      let pRight = nums.length - 1

      const target = -nums[i]

      while (pLeft < pRight) {
        const sum = nums[pLeft] + nums[pRight]
        if (sum < target) {
          pLeft += 1
        } else if (sum > target) {
          pRight -= 1
        } else {
          res.push([nums[pLeft], nums[pRight], nums[i]])
          pLeft += 1
          while (pLeft < pRight && nums[pLeft] === nums[pLeft - 1]) {
            pLeft += 1
          }
        }
      }
    }

    return res
  }
}

// const nums = [-1,0,1,2,-1,-4]
// const nums = [0,1,1]
// const nums = [0,0,0]
const nums = [0,0,0,0]

const res = new Solution().threeSum(nums)

console.log('Result: ', res)
