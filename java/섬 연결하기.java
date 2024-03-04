import java.util.*;

class Solution {
    
    static int[] parents;
    public int solution(int n, int[][] costs) {
        int answer = 0;
        
        parents = new int[n];
        for (int i = 0 ; i < n ; i++) {
            parents[i] = i;
        }
        
        Arrays.sort(costs, (o1, o2) -> (o1[2] - o2[2]));
        
        for (int[] c : costs) { 
            if (find(c[0]) != find(c[1])) {
                answer += c[2];
                union(c[0], c[1]);
            } 
        }
        
        return answer;
    }
    
    public static int find(int p) {
        if (parents[p] != p) {
            return find(parents[p]);
        }
        return parents[p];
    }
    
    public static void union(int a, int b) {
        
        int pa = find(a);
        int pb = find(b);
        
        if (pa > pb) {
            parents[pa] = pb;
        } else {
            parents[pb] = pa;
        }
    }
}
