import java.util.*;

class Solution {
    public int solution(int[][] routes) {
        int answer = 0;
        
        Arrays.sort(routes, (o1, o2) -> (o1[1] - o2[1]));
        
        int pos = routes[0][1];
        answer += 1;
        for (int i = 1 ; i < routes.length ; i++) {
            if (routes[i][0] <= pos && pos <= routes[i][1]) {
                continue;
            } else {
                pos = routes[i][1];
                answer += 1;
            }
        }
        
        return answer;
    }
}

