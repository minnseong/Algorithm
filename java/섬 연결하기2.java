import java.util.*;

class Solution {
    public int solution(int n, int[][] costs) {
        int answer = 0;
        
        Arrays.sort(costs, (o1, o2) -> (o1[2] - o2[2]));
        
        int[] parents = new int[n];
        for (int i = 0 ; i < n ; i++) {
            parents[i] = i;
        }
        
        for (int[] cost : costs) {
            if (find(cost[0], parents) != find(cost[1], parents)){
                answer += cost[2];
                union(cost[0], cost[1], parents);
            }
        }
        
        return answer;
    }
    
    public int find(int x, int[] parent) {
        if (parent[x] != x) {
            return find(parent[x], parent);
        }
        return parent[x];
    }

    public void union(int x, int y, int[] parent) {
        
        int px = find(x, parent);
        int py = find(y, parent);
        
        if (px < py) {
            parent[py] = px;
        } else {
            parent[px] = py;
        }
    }
}
