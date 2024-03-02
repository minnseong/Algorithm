import java.util.*;

class Solution {
    
    static boolean[] visited;
    static String[] _words;
    static int answer;
    static String _target;
    
    public int solution(String begin, String target, String[] words) {
        
        answer = Integer.MAX_VALUE;
        visited = new boolean[words.length];
        _words = words;
        _target = target;
        
        dfs(begin, 0);
        
        if (answer == Integer.MAX_VALUE) {
            return 0;
        }
        return answer;
    }
    
    public static void dfs(String cursor, int cnt) {
        
        if (cursor.equals(_target)) {
            if (answer > cnt) {
                answer = cnt;
            }
        }
        
        for (int i = 0 ; i < _words.length ; i++) {
            if (!visited[i] && check(cursor, _words[i])) {
                visited[i] = true;
                dfs(_words[i], cnt+1);
                visited[i] = false;
            }
        }
    }
    
    public static boolean check(String s1, String s2) {
        
        int cnt = 0;
        for (int i = 0 ; i < s1.length() ; i++) {
            if (s1.charAt(i) == s2.charAt(i)) {
                cnt += 1;
            }
        }
        
        if (cnt == (s1.length()-1)) return true;
        else return false;
    }

}
