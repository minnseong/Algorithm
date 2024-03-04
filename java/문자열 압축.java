import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = Integer.MAX_VALUE;
        
        if (s.length() == 1) {
            return 1;
        }
        
        for (int i = 1 ; i <= s.length() / 2 ; i++) {
             
            List<String> split = new ArrayList<>();
            
            int idx = 0;
            for (int j = 0 ; j < s.length() / i ; j++) {
                split.add(s.substring(idx, idx+i));
                idx += i;
            }
            if (s.substring(idx, s.length()).length() >= 1) {
                split.add(s.substring(idx, s.length()));
            }
            split.add("");
            
            int cnt = 1;
            int ans = 0;
            for (int j = 0; j < split.size()-1 ; j++) {
                if (split.get(j).equals(split.get(j+1))) {
                    cnt += 1;
                } else {
                    if (cnt == 1) {
                        ans += split.get(j).length();
                    }
                    else {
                        ans += (split.get(j).length() + String.valueOf(cnt).length());
                        cnt = 1;
                    }
                }
            }
            
            if (answer > ans) {
                answer = ans;
            }
        }
        
        return answer;
    }
}
