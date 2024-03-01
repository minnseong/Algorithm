import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        
        Arrays.sort(people);
        
        int l = 0;
        int r = people.length - 1;
        
        while (l <= r) {
            if (people[l] + people[r] <= limit) {
                answer += 1;
                l += 1;
                r -= 1;
            } else {
                r -= 1;
                answer += 1;
            }
        }
        
        return answer;
    }
}
