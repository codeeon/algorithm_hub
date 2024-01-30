function solution(nums) {
    // let cnt = nums.length;
    let answer = 0;
    
    const pkm = {};
    // let largest = 0;
    
    for(let i = 0; i < nums.length; i++) {
        pkm[nums[i]] = 1;
    }
    
    if(nums.length / 2 >= Object.keys(pkm).length) {
        answer = Object.keys(pkm).length;
    } else {
        answer = nums.length / 2;
    }
    
    return answer;
}
    
//     const pkmList = {...pkm};
//     // console.log(pkmList);
    
//     for(let i of nums) {
//         pkm[i].push(i);
//     }
    
//     while(cnt > 0) {
//         for(let key in pkm) {
//             if(pkm[key].length > 0) {
//                 pkmList.push(pkm[key].pop);
//                 cnt--;
                
//             }
//         }
//     }
    
//     console.log(pkm);
    
    
    
    
    
//     return answer;
// }