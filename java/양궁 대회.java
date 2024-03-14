import java.util.*;

class Solution {
    
    static int[] score;
    static boolean[] visited;
    static boolean[] answer = new boolean[11];
    static int maxScore;
    static int m;
    
    public int[] solution(int n, int[] info) {
        
        score = new int[11];
        visited = new boolean[11];
        m = n;
        maxScore = 0;
        
        for (int i = 0 ; i < 11 ; i++) {
            score[i] = info[i] + 1;   
        }
        
        dfs(score, info, 0);
        int cnt = 0;
        int[] ans = new int[11];
        for (int i = 0 ; i < 11 ; i++) {
            if (answer[i]) {
                cnt += score[i];
                ans[i] = score[i];
            }
        }
        
        if (cnt == 0) {
            return new int[] {-1};
        } else if (cnt < n) {
            ans[10] += (n-cnt);
        }
        
        return ans;
    }
    
    public static void dfs(int[] lion, int[] apeach, int used) {
        
        if (used > m) {
            return;
        }
        else {
            int lionScore = 0;
            int apeachScore = 0;
            for (int j = 0 ; j < 11 ; j++) {
                if (visited[j]) {
                    lionScore += (10 - j);
                } else if (apeach[j] >= 1) {
                    apeachScore += (10 - j);
                }
            }
            
            if (lionScore > apeachScore && (lionScore-apeachScore) >= maxScore) {
                answer = visited.clone();
                maxScore = lionScore-apeachScore;
            }
        }
        
        for (int i = 0 ; i < 11 ; i++) {
            if (!visited[i]) {
                visited[i] = true;
                dfs(lion, apeach, used+lion[i]);
                visited[i] = false;
            }
        }
    }
}
