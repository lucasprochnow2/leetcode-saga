class Solution {
  longestConsecutive(nums: number[]): number {
    if (!nums.length) return 0
    let res = 1
    const initKeys: string[] = []

    const sortedNums = [...new Set(nums.sort((a, b)=> (a-b)))]

    for (let k in sortedNums) {
      const num = sortedNums[k]
      if (!sortedNums.includes(num - 1)) initKeys.push(k)
    }

    console.log(sortedNums)
    console.log(initKeys)

    let consecutive = 0
    for (let i in sortedNums) {
      if (initKeys.includes(i)) {
        consecutive = 1
        continue;
      }

      const currNum = sortedNums[i]
      const prevNum = sortedNums[parseInt(i) - 1]
      if (prevNum === currNum - 1) {
        consecutive += 1
        res = Math.max(res, consecutive);
      }
    }

    return res
  }
}

// const nums = [2,20,4,10,3,4,5]
// const nums = [0,3,2,5,4,6,1,1]
const nums = [9,1,4,7,3,-1,0,5,8,-1,6]

const res = new Solution().longestConsecutive(nums);

console.log('Result', res)
