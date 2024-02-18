const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = +input.shift();
const [start, target] = input
  .shift()
  .split(' ')
  .map((v) => +v);
const M = +input.shift();
const Edge = input.map((v) => v.split(' ').map((item) => +item));

// 2차원 배열 생성
const graph = [...Array(N + 1)].map((e) => []);

// 2차원 배열 그래프
for (let i = 0; i < M; i++) {
  const [a, b] = Edge[i];
  graph[a].push(b);
  graph[b].push(a);
}

const dfs = (start, target) => {
  const visited = Array(N + 1).fill(false);
  visited[start] = true;
  const stack = [[start, 0]];

  while (stack.length) {
    const [number, cnt] = stack.pop();

    if (number === target) return cnt;

    if (graph[number]) {
      graph[number].forEach((next) => {
        if (!visited[next]) {
          visited[next] = true;
          stack.push([next, cnt + 1]);
        }
      });
    }
  }
  return -1;
};

console.log(dfs(start, target));