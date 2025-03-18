function binarySearch(nums, target) {
  let left = 0,
    right = nums.length - 1,
    steps = 0

  while (left <= right) {
    steps++
    let mid = Math.floor((left + right) / 2)

    if (nums[mid] === target) {
      console.log('steps:', steps)
      return mid
    }

    if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1
    }

  }

  return -1

}

const numsaysToTest = [
  { nums: [1, 2, 3, 4, 5], target: 3 }, // numsay com números inteiros
  { nums: [10, 20, 30, 40, 50], target: 25 }, // numsay com números inteiros, alvo não presente
  { nums: [-10, -5, 0, 5, 10], target: -5 }, // numsay com números negativos e positivos
  { nums: [1.1, 2.2, 3.3, 4.4, 5.5], target: 4.4 }, // numsay com números decimais
  { nums: ['a', 'b', 'c', 'd', 'e'], target: 'c' }, // numsay com caracteres
  { nums: [], target: 1 }, // numsay vazio
  { nums: [1], target: 1 }, // numsay com um único elemento
];

numsaysToTest.forEach(test => {
  const result = binarySearch(test.nums, test.target);
  console.log(`Array: ${test.nums}, Target: ${test.target}, Result: ${result}`);
});