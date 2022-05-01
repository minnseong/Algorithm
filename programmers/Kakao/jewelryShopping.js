// Programmers 05/01 2022
// 보석 쇼핑

function solution(gems) {
    var answer = [];
    var gems_dict = {}
    var gems_cnt = (new Set(gems)).size

    let i = 0;
    let j = 0;
    
    gems_dict[gems[i]] = 1
    while (i < gems.length && j < gems.length) {
        if (Object.keys(gems_dict).length < gems_cnt) {
            j += 1
            if (j >= gems.length)
                break
            if (gems[j] in gems_dict) {
                gems_dict[gems[j]] += 1
            } else {
                gems_dict[gems[j]] = 1
            }
        }
        else {
            answer.push([i+1, j+1])
            if (gems_dict[gems[i]] == 1) {
                delete gems_dict[gems[i]]
            }
            else {
                gems_dict[gems[i]] -= 1
            }
            i += 1
        }
    }
    answer.sort(function(x) {
        return x[1]-x[0]
    });
    return answer[0];
}

console.log(solution(["AA", "AB", "AC", "AA", "AC"]))