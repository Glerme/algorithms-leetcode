/**
 * @param {number[]} arr
 * @param {number} target
 * @return {number[]}
 */
const twoSum = function (arr, target) {
  let obj = {};

  for (let index = 0; index < arr.length; index++) {
    let complement = target - arr[index];
    console.log(complement);

    if (obj[complement] !== undefined) {
      return [obj[complement], index];
    }

    obj[arr[index]] = index;
  }
};

console.log(twoSum([2, 7, 11, 15], 9));
console.log(twoSum([3, 2, 4], 6));
console.log(twoSum([3, 3], 6));
