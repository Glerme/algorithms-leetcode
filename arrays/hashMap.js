/**
 * @param {string} s
 * @return {number}
 */
function firstUniqueChar(s) {
  let d = {};

  for (const [index, char] of [...s].entries()) {
    if (!d[char]) {
      d[char] = [index, 1];
    } else {
      d[char][1] += 1;
    }
  }

  for (const key in d) {
    const element = d[key];

    if (element[1] === 1) {
      return element[0];
    }
  }

  return -1;
}

console.log(firstUniqueChar("leetcode"));
console.log(firstUniqueChar("loveleetcode"));