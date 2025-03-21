const fs = require('fs');
 const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
 const input = fs.readFileSync(filePath).toString().trim().split('\n');
 
 const numberA = +input.shift();
 const stringNumberB = input.shift();

 for (let i = 0; i < stringNumberB.length; i++) {
    const cnt = numberA * parseInt(stringNumberB.at(stringNumberB.length - 1 - i));
    console.log(cnt);
 }
 console.log(numberA * parseInt(stringNumberB));