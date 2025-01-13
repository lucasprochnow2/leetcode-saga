class Solution {
  /**
   * @param {number[]} nums
   * @return {number[]}
   */
  productExceptSelf(nums: number[]): number[] {
    const n = nums.length;
    const res = new Array(n);
    const pref = new Array(n);
    const suff = new Array(n);

    pref[0] = 1;
    suff[n - 1] = 1;
    for (let i = 1; i < n; i++) {
      pref[i] = nums[i - 1] * pref[i - 1];
    }
    for (let i = n - 2; i >= 0; i--) {
      suff[i] = nums[i + 1] * suff[i + 1];
    }
    for (let i = 0; i < n; i++) {
      res[i] = pref[i] * suff[i];
    }

    return res;
  }
}

const nums = [1,2,4,6] // [48,24,12,8]
// const nums = [-1,0,1,2,3] // [0,-6,0,0,0]

const solution = new Solution().productExceptSelf(nums)

console.log('Result: ', solution)
