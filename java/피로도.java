import java.util.*;

class Solution {
    
    static boolean[] visited;
    static int[] arr;
    static List<Integer> answer;
    
    public int solution(int k, int[][] dungeons) {
        
        answer = new ArrayList<>();
        visited = new boolean[dungeons.length];
        arr = new int[dungeons.length];
        
        explore(0, k, dungeons);
        
        return Collections.max(answer);
    }
    
    public static void explore(int x, int k, int[][] dungeons) {
        
        if (x == arr.length) {
            int tmp = k;
            
            int ans = 0;
            for (int idx : arr) {
                if (tmp >= dungeons[idx][0]) {
                    tmp -= dungeons[idx][1];
                    ans += 1;
                }
            }
            
            answer.add(ans);
            return;
        }
        
        for (int i = 0 ; i < arr.length ; i++) {
            if(!visited[i]) {
                arr[x] = i;
                visited[i] = true;
                explore(x+1, k, dungeons);
                visited[i] = false;
            }
        }
        
    }
}
