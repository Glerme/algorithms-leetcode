/**
 * @param {number[]} arr
 * @param {number} target
 * @return {boolean}
 */
const containsNearbyDuplicate = function (arr, target) {
  let l = 0;
  let r = 0;

  let uniqueElementsSet = new Set();

  while (r < arr.length) {
    if (uniqueElementsSet.has(arr[r])) {
      return true;
    }

    uniqueElementsSet.add(arr[r]);

    if (r - l >= target) {
      uniqueElementsSet.delete(arr[l]);
      l++;
    }

    r++;
  }

  return false;
};

console.log(containsNearbyDuplicate([1, 2, 3, 1], 3)); // true
console.log(containsNearbyDuplicate([1, 0, 1, 1], 1)); // true
console.log(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)); // false
