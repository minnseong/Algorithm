import java.util.*;

class Solution {
    
    public int solution(int n, int[][] edge) {
        int answer = 0;
        
        Map<Integer, Set<Integer>> graph = new HashMap<>();
        boolean[] visited = new boolean[n+1];
        int[] distFromStart = new int[n+1];
        
        for (int i = 1 ; i <= n ; i++) {
            graph.put(i, new HashSet<>());
        }
        
        for (int[] e : edge) {
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }
        
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] {1, 0});
        visited[1] = true;
        
        while(!queue.isEmpty()) {
            
            int[] node = queue.poll();
            int pos = node[0];
            int dist = node[1];
            
            for (Integer next : graph.get(pos)) {
                if (!visited[next]) {
                    distFromStart[next] = dist + 1;
                    queue.add(new int[] {next, dist+1});
                    visited[next] = true;
                }
            }
        }
        
        int maxDist = 0;
        for (int dist : distFromStart) {
            if (maxDist < dist) {
                maxDist = dist;
            }
        }
        
        for (int dist : distFromStart) {
            if (maxDist == dist) {
                answer += 1;
            }
        }
        
        return answer;
    }
}
