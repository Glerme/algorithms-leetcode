function reverseWordsTwoPointers(s) {
  const arr = s.split('');
  let start = 0;

  for (let end = 0; end <= arr.length; end++) {
    if (end === arr.length || arr[end] === ' ') {
      let left = start;
      let right = end - 1;
      while (left < right) {
        [arr[left], arr[right]] = [arr[right], arr[left]];
        left++;
        right--;
      }
      start = end + 1;
    }
  }
  return arr.join('');
}

function reverseWordsMap(s) {
  return s.split(" ").map(char => char.split('').reverse().join('')).join(' ');
}

// Teste com string grande
const testString = "Let's take LeetCode contest ".repeat(10000);

// Benchmark Two Pointers
console.time('Two Pointers');
reverseWordsTwoPointers(testString);
console.timeEnd('Two Pointers');

// Benchmark Map
console.time('Map');
reverseWordsMap(testString);
console.timeEnd('Map');
