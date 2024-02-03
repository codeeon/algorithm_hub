const solution = s => {
    const arr = [...s];
    const result = [-1];

    for (let i = 1; i < arr.length; i++) {
        const newArr = arr.slice(0, i);
        const item = newArr.lastIndexOf(arr[i]);
        item === -1 ? result.push(-1) : result.push(i - item);
        }
    return result;
}