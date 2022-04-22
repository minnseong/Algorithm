// Programmers 04/22 2022
// 약수의 개수와 덧셈

function countDivisor(num) {
    let cnt = 0;
    
    for (let i = 0 ; i < num ; i++) {
        if (num % i == 0) {
            cnt++;
        } 
    }   
    if (cnt & 1) {
        return false;
    }
    return true;
}

function solution(left, right) {
    var answer = 0;
    
    for (let i = left ; i <= right ; i++) {
        if (countDivisor(i)) {
            answer -= i
        }
        else {
            answer += i
        }
    }
    return answer;
}
