const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [a, b] = input.shift().split(' ').map(Number);

const solution = (a, b) => {
  let cnt = 0;

  let arr = Array(a + 1)
    .fill(0)
    .map((v) => true);

  for (let i = 2; i <= a; i++) {
    if (arr[i]) {
      for (let j = 1; i * j <= a; j++) {
        arr[i * j] ? cnt++ : null;
        if (cnt === b) return i * j;
        arr[i * j] = false;
      }
    }
  }
};

console.log(solution(a, b));
