class Solution {
  private sep = "#"

  encode(strs: string[]): string {
    let result = ""

    for (const k in strs)
      result += `${strs[k].length}${this.sep}${strs[k]}`

    return result
  }

  decode(str: string): string[] {
    const result: string[] = []
    const letters = str.split("")

    let befSep = true
    let currLen = ''
    let currWord = ''
    let currCount = 0
    let isSep = false

    for (let i = 0; i < letters.length; i++) {
      const letter = letters[i]

      if (letter === this.sep && befSep) {
        befSep = false
        isSep = true
      } else
        isSep = false

      if (befSep)
        currLen += letter
      else if (!isSep)
        currCount += 1

      if (currCount > 0)
        currWord += letter

      if (
        (currCount === parseInt(currLen) && parseInt(currLen) > 0) ||
        (isSep && currLen === '0')
      ) {
        // console.log('--- caiu')
        result.push(currWord)
        befSep = true
        currLen = ''
        currWord = ''
        currCount = 0
      }
    }

    return result
  }
}

// const strs = ["neet","code","love","you"]
// const strs = ["we","say",":","yes","!@#$%^&*()"]
const strs = ["","   ","!@#$%^&*()_+","LongStringWithNoSpaces","Another, String With, Commas"]

const resEncode = new Solution().encode(strs)
const resDecode = new Solution().decode(resEncode)

console.log('Result encode: ', resEncode)
console.log('Result decode: ', resDecode)
