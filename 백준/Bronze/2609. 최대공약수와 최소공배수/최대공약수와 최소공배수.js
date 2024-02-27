const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [a, b] = input.shift().split(' ').map(Number);

const solution = (a, b) => {
  let x = Math.max(a, b);
  let y = Math.min(a, b);

  let gcd = 1;
  let lcm = x * y;

  for (let i = y; i > 0; i--) {
    if (x % i === 0 && y % i === 0) {
      gcd = i;
      break;
    }
  }
  for (let i = x; i <= lcm; i += x) {
    if (i % x === 0 && i % y === 0) {
      lcm = i;
      break;
    }
  }

  return `${gcd}\n${lcm}`;
};

console.log(solution(a, b));
