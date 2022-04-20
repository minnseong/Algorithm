// Programmers 04/20 2022
// Javascript - 모의고사

function solution(answers) {
    var answer = [];
    
    let cnt = [0, 0, 0];
    let a1= [1,2,3,4,5]
    let a2= [2,1,2,3,2,4,2,5];
    let a3= [3,3,1,1,2,2,4,4,5,5];
    
    for (let i = 0 ; i < answers.length ; i++) {
        if (answers[i] == a1[i%5])
            cnt[0] += 1;
        if (answers[i] == a2[i%8])
            cnt[1] += 1;
        if (answers[i] == a3[i%10])
            cnt[2] += 1;
    }
    
    let maxCnt = Math.max(...cnt);
    for (let i = 0; i < 3 ; i++){
        if (maxCnt == cnt[i]) {
            answer.push(i+1)
        }
    }
    return answer;
}

console.log(solution([1,2,3,4,5]))