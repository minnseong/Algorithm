import java.util.*;

class Solution {
    
    static String[] s = new String[] {"A", "E", "I", "O", "U"};
    static int answer;
    static int cnt = 0;
    
    public int solution(String word) {
        
        answer = 0;
        dfs(new StringBuilder(), word);
        
        return answer;
    }
    
    public static void dfs(StringBuilder sb, String word) {
        
        if (sb.length() > 5) {
            cnt -= 1;
            return;
        }
        
        if (sb.toString().equals(word)) {
            answer = cnt;
            return;
        }
        
        for (int i = 0 ; i < 5 ; i++) {
            sb.append(s[i]);
            cnt += 1;
            dfs(sb, word);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}
