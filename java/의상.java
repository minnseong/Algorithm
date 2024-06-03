import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        Map<String, Integer> map = new HashMap<>();
        
        for (String[] cloth : clothes) {
            map.put(cloth[1], map.getOrDefault(cloth[1], 0) + 1);
        }
        
        for (Integer cnt : map.values()) {
            answer *= (cnt + 1);
        }
        
        answer -= 1;
        return answer;
    }
}
