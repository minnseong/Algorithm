// Programmers 04/21 2022
// Javascript - k 번째수

function solution(array, commands) {
    var answer = [];
    
    for (let i in commands) {
        let splitArray = array.slice(commands[i][0]-1, commands[i][1])
        splitArray.sort(((a,b) => a - b))
        answer.push(splitArray[commands[i][2]-1])
    }
    return answer;
}