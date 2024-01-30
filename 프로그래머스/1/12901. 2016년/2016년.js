function solution(a, b) {
    const cal = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    const week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    let cnt = 0
    
    cnt = cal.filter((v, i) => i < a).reduce((acc, cur) => acc + cur, 0);
    cnt += b - 1    

    return week[cnt % 7];
}