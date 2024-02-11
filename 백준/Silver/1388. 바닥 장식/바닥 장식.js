const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt'; // 리눅스(백준) 경로와, IDE 사용 시 경로(텍스트 인풋)
let input = fs.readFileSync(filePath).toString().split('\n');

const inputC = input[0].split(' ').map((v) => +v);
const inputCase = input.filter((v) => v !== input[0]).map((v) => v.split(''));

const solution = (testCase) => {
  let cnt = 0;

  for (let i = 0; i < inputC[0]; i++) {
    for (let j = 0; j < inputC[1]; j++) {
      if (testCase[i][j] == '0') continue;
      else if (testCase[i][j] === '-') {
        for (let x = j; x < inputC[1]; x++) {
          if (testCase[i][x] === '-') {
            testCase[i][x] = '0';
          } else break;
        }
        cnt++;
      } else if (testCase[i][j] === '|') {
        for (let y = i; y < inputC[0]; y++) {
          if (testCase[y][j] === '|') {
            testCase[y][j] = '0';
          } else break;
        }
        cnt++;
      }
    }
  }
  return cnt;
};

console.log(solution(inputCase));
