const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const T = +input.shift();

let result = '';

for (let i = 0; i < T; i++) {
  const N = +input.shift();
  const Case = input.shift().split(' ').map(Number);
  const M = +input.shift();
  const Case2 = input.shift().split(' ').map(Number);

  const setCase = new Set(Case);

  const solution = () => {
    let result = [];
    for (const i of Case2) {
      setCase.has(i) ? result.push(1) : result.push(0);
    }
    return result.join('\n');
  };

  console.log(solution());
}