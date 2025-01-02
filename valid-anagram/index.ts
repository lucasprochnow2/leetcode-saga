class Solution {

  /**
   * MY SOLUTION
   */
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
   * Sorting solution
  */
  isAnagram2(s: string, t: string): boolean {
    if (s.length !== t.length) {
      return false;
    }

    let sSort = s.split("").sort().join();
    let tSort = t.split("").sort().join();

    return sSort == tSort
}
}

const solution = new Solution()

const s = "racecar"
const t = "carrace"

console.log('Result: ', solution.isAnagram(s, t))
