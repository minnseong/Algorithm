// Programmers 04/29 2022
// Kakao 숫자 문자열과 영단어

function solution(s) {
    var answer = "";
    
    var numDict = {'zero' : 0, 'one' :1, 'two' :2, 'three':3, 'four':4, 'five' :5,
                'six':6,'seven':7,'eight':8, 'nine':9}
    
    let tmp = "";
    for (let i  = 0 ; i < s.length ; i++) {
        if (!isNaN(s[i])) {
            answer += String(s[i])
            tmp = ""
        }
        else {
            tmp += s[i]
            if (tmp in numDict) {
                answer += String(numDict[tmp])
                tmp = ""
            }
        }
    }
    return Number(answer);
}

console.log(solution("23four5six7")) 