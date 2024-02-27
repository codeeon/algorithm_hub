const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [a, b] = input.shift().split(' ').map(Number);

//  유클리드 호제법
const findGcd = (a, b) => {
  const remainder = a % b;
  if (remainder === 0) return b;
  return findGcd(b, remainder);
};

let lcm = (a * b) / findGcd(a, b);

const solution = (a, b) => {
  return `${findGcd(a, b)}\n${lcm}`;
};

console.log(solution(a, b));