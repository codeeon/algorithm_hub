const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = +input.shift();
const Case = input.shift().split(' ').map(Number);

const CaseSet = new Set([...Case]);

const M = +input.shift();
const Case2 = input.shift().split(' ').map(Number);

const solution = () => {
  const result = [];

  for (const i of Case2) {
    CaseSet.has(i) ? result.push(1) : result.push(0);
  }

  return result.join(' ');
};

console.log(solution());
