import java.util.*;

class Solution {

    static Map<Integer, List<Integer>> networks;
    static boolean[] visited;
    
    public int solution(int n, int[][] computers) {
        
        int answer = 0;
        networks = new HashMap<Integer, List<Integer>>();
        visited = new boolean[n];
        
        for (int i = 0 ; i < n ; i++) {
            networks.put(i, new ArrayList<>());
            for (int j = 0 ; j < n ; j++) {
                if (computers[i][j] == 1 && i != j) {
                    networks.get(i).add(j);
                }
            }
        }
        
        for (int i = 0 ; i < n ; i++) {
            if (!visited[i]) {
                dfs(i);
                answer += 1;
            }
        }
    
        return answer;
    }
    
    public static void dfs(int x) {
        
        if (!visited[x]) {
            visited[x] = true;
            for (int i : networks.get(x)) {
                dfs(i);
            }
        }
    }
}
