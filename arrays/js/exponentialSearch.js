
/**
 * @param {Array<number>} arr
 * @param {number} target
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
function binarySearch(arr, target, left, right) {
  let steps = 0

  while (left <= right) {
    steps++
    let mid = Math.floor((left + right) / 2)

    if (arr[mid] === target) {
      console.log('steps:', steps)
      return mid
    }

    if (arr[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1
    }

  }
  return -1
}

/**
 * @param {Array<number>} arr
 * @param {number} target
 * @return {number}
 */
function exponentialSearch(arr, target) {
  if (arr[0] === target) {
    return 0
  }

  let arrLength = arr.length
  let i = 1

  while (i < arrLength && arr[i] < target) {
    i *= 2
  }

  if (i < arrLength && arr[i] === target) {
    return i
  }

  return binarySearch(arr, target, Math.floor(i / 2), Math.min(i, arrLength - 1));
}

const arr = Array.from({ length: 40 }, (_, i) => i + 1);
const target = 32;
const result = exponentialSearch(arr, target);
console.log(`Target: ${target}, Result: ${result}`);