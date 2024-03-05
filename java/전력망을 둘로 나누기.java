import java.util.*;

class Solution {
    
    static Map<Integer, Set<Integer>> graph;
    static int count;
    
    public int solution(int n, int[][] wires) {
        
        int answer = Integer.MAX_VALUE;
        
        count = n;
        graph = new HashMap<>();
        
        for (int i = 1 ; i <= n ; i++) {
            graph.put(i, new HashSet<>());
        }
        
        for (int[] wire : wires) {
            graph.get(wire[0]).add(wire[1]);
            graph.get(wire[1]).add(wire[0]);
        }
        
        for (int[] wire : wires) {
            
            graph.get(wire[0]).remove(wire[1]);
            graph.get(wire[1]).remove(wire[0]);
            
            int a_cnt = bfs(wire[0]);
            int b_cnt = n - a_cnt;
            
            if (Math.abs(a_cnt - b_cnt) < answer) {
                answer = Math.abs(a_cnt - b_cnt);
            }
            
            graph.get(wire[0]).add(wire[1]);
            graph.get(wire[1]).add(wire[0]);
        }
        
        
        return answer;
    }
    
    public static int bfs(int x) {
        
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[count+1];
        visited[x] =true;
        queue.add(x);
        int cnt = 1;
        
        while(!queue.isEmpty()) {
            
            int next = queue.poll();
            
            for (Integer n : graph.get(next)) {
                if (!visited[n]) {
                    queue.add(n);
                    cnt += 1;
                    visited[n] = true;
                }
            }
        }
        
        return cnt;
    }
}
