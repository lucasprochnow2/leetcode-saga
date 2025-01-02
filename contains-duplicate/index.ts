class Solution {
  /**
   * Solution comparing Set size with nums length
   * Time complexity: O(n)
   * Space complexity: O(n)
   */
  hasDuplicate(nums: number[]): boolean {
    return new Set(nums).size < nums.length;
  }

  /**
   * Solution iteration through nums checking if Set has its value
   * Time complexity: O(n)
   * Space complexity: O(n)
   */
  hasDuplicate2(nums: number[]): boolean {
    const seen = new Set();

    for (const num of nums) {
      if (seen.has(num)) {
        return true;
      }
      seen.add(num);
    }

    return false;
  }
}


const solution = new Solution()

const nums = [1, 2, 3, 3] // true
const nums2 = [1, 2, 3, 4] // false

console.log('Result', solution.hasDuplicate(nums2))
