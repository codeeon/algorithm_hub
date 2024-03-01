const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = +input.shift();
const Case = input.shift().split(' ').map(Number);
// Case.sort((a, b) => a - b);
const setCase = new Set(Case);
// console.log(setCase)

const M = +input.shift();
const Case2 = input.shift().split(' ').map(Number);

const solution = () => {
  let result = [];
  for (const i of Case2) {
    // result.push(BinarySearch(i));
    setCase.has(i) ? result.push(1) : result.push(0)
  }
  return result.join('\n');
};

// const BinarySearch = (val) => {
//   let start = 0;
//   let end = Case.length - 1;

//   while (start <= end) {
//     let mid = Math.trunc((start + end) / 2);

//     if (val === Case[mid]) {
//       return 1;
//     } else if (val < Case[mid]) {
//       end = Case[mid] - 1;
//     } else {
//       start = Case[mid] + 1;
//     }
//   }

//   return 0;
// };

console.log(solution());
