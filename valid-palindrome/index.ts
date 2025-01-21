class Solution {
  isPalindrome(s: string): boolean {
    const str = s.toLowerCase().replace(/[^a-z0-9]/g, '');
    let res = true
    let p2 = str.length - 1

    for (let k in str.split('')) {
      console.log(k, p2)
      console.log('-', str[k], str[p2])
      if (str[k] !== str[p2]) res = false
      console.log('---', res)
      p2 -= 1

      if (parseInt(k) > p2) break;
    }

    return res
  }
}

const str = "Was it a car or a cat I saw?"
// const str = "tab a cat"

const res = new Solution().isPalindrome(str)

console.log('Result', res)
