import java.util.*;

class Solution {
    
    public int solution(int n, int[][] results) {
        int answer = 0;
        
        Map<Integer, Set<Integer>> wins = new HashMap<>();
        Map<Integer, Set<Integer>> loses = new HashMap<>();
        
        for (int i = 1 ; i <= n ; i++) {
            wins.put(i, new HashSet<>());
            loses.put(i, new HashSet<>());
        }
        
        for (int[] result : results) {
            wins.get(result[0]).add(result[1]);
            loses.get(result[1]).add(result[0]);
        }
       
        for (int i = 1 ; i <= n ; i++) {
            bfs(i, n, wins);
            bfs(i, n, loses);
        }
        
        for (int i = 1 ; i <= n ; i++) {
            if (wins.get(i).size() + loses.get(i).size() == (n-1)) {
                answer += 1;
            }
        }
        
        return answer;
    }
    
    public static void bfs(int start, int n, Map<Integer, Set<Integer>> map) {
        
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[n+1];
        
        queue.add(start);
        visited[start] = true;
        Set<Integer> set = new HashSet<>();
        
        while(!queue.isEmpty()) {
            
            int next = queue.poll();
            
            for (int i : map.get(next)) {
                if (!visited[i]) {
                    queue.add(i);
                    set.add(i);
                    visited[i] = true;
                }
            }
        }
        
        map.get(start).addAll(set);
    }
}
  
