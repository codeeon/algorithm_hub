const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

while (true) {
  const [w, h] = input
    .shift()
    .split(' ')
    .map((v) => +v);

  if (w === 0 || h === 0) break;

  const graph = [];
  for (let i = 0; i < h; i++) {
    graph.push(
      input
        .shift()
        .split(' ')
        .map((v) => +v)
    );
  }
  //   console.log(graph);
  const visited = Array(h)
    .fill(0)
    .map((v) => Array(w).fill(false));
  //   console.log(visited);

  const dfs = (x, y) => {
    const dx = [-1, -1, -1, 0, 0, 1, 1, 1];
    const dy = [-1, 0, 1, -1, 1, -1, 0, 1];
    visited[x][y] = true;

    for (let i = 0; i < dx.length; i++) {
      const [X, Y] = [x + dx[i], y + dy[i]];

      if (X >= 0 && X < h && Y >= 0 && Y < w) {
        if (graph[X][Y] === 1 && visited[X][Y] === false) {
          dfs(X, Y);
        }
      }
    }

    return;
  };

  let cnt = 0;

  for (let i = 0; i < h; i++) {
    for (let j = 0; j < w; j++) {
      if (graph[i][j] === 1 && visited[i][j] === false) {
        dfs(i, j);

        cnt++;
      }
    }
  }
  console.log(cnt);
}