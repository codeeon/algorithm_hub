const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const S = +input.shift();

const solution = (S) => {
  let maxNum = Math.sqrt(2 * S);

  for (let i = Math.floor(maxNum); i >= 0; i--) {
    if ((i * i) + i <= 2 * S) return i;
  }
};

console.log(solution(S));
