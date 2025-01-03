class Solution {
  isAnagram(s: string, t: string): boolean {
    // check if strings sizes are equal
    if (s.length !== t.length) return false

    const hashS = {}
    const hashT = {}

    const Ssplit = s.split('')
    const Tsplit = t.split('')

    for (let i = 0; i < s.length; i++) {
      const valS = Ssplit[i]
      const valT = Tsplit[i]

      if (!hashS[valS]) hashS[valS] = 1
      else hashS[valS] += 1

      if (!hashT[valT]) hashT[valT] = 1
      else hashT[valT] += 1
    }

    for (const key in hashS) {
      if (hashS[key] !== hashT[key]) return false
    }

    return true
  }

  /**
   * Brute force solution (First I had idea)
   */
  groupAnagrams(strs: string[]): string[][] {
    const res: string[][] = []
    const alreadyUsed = new Map()

    for (let i = 0; i < strs.length; i++) {
      const currStr = strs[i]
      const currRes = [currStr]

      if (alreadyUsed.has(currStr)) continue

      for (let z = 0; z < strs.length; z++) {
        if (i === z) continue

        if (this.isAnagram(currStr, strs[z])) {
          currRes.push(strs[z])
          alreadyUsed.set(strs[z], z)
        }
      }

      res.push(currRes)
      alreadyUsed.set(currStr, i)
    }

    return res
  }

  /** Optimal solution */
  groupAnagrams2(strs: string[]): string[][] {
    const res = {};

    for (let s of strs) {
      const count = new Array(26).fill(0);
      for (let c of s) {
        count[c.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
      }

      const key = count.join(',');
      console.log('--', s, count, key)
      if (!res[key]) {
        res[key] = [];
      }

      res[key].push(s);
    }
    return Object.values(res);
  }
}

const solution = new Solution()

const strs = ["act","pots","tops","cat","stop","hat"]
// const strs = ["x"]
// const strs = [""]

console.log('Result: ', solution.groupAnagrams2(strs))
