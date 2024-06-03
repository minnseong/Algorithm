import java.util.*;

class Solution {
    
    static boolean[] visited;
    static int answer;
    static Map<Integer, List<Integer>> graph;
    
    public int solution(int n, int[][] computers) {
        
        answer = 0;
        visited = new boolean[n+1];
        graph = new HashMap<>();
        
        for (int i = 0 ; i < n ; i++) {
            graph.put(i+1, new ArrayList<>());
        }
        
        for (int i = 0 ; i < n ; i++) {
            for (int j = 0 ; j < n ; j++) {
                if (i == j) {
                    continue;
                }
                
                if (computers[i][j] == 1) {
                    graph.get(i+1).add(j+1);
                }
            }
        }
        
        for (int i = 1 ; i < n+1 ; i++) {
            if (!visited[i]) {
                dfs(i);
                answer += 1;
            }
        }
        
        return answer;
    }
    
    public void dfs(int x) {
        visited[x] = true;
        for (Integer next : graph.get(x)) {
            if (!visited[next]) {
                dfs(next);
            }
        }
    }
}
