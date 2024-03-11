import java.util.*;

class Solution {
    public int solution(int n, int s, int a, int b, int[][] fares) {
        
        Map<Integer, List<Integer[]>> graph = new HashMap<>();

        for (int i = 1 ; i <= n ; i++) {
            graph.put(i, new ArrayList<>());
        }
        
        int[][] map = new int[n+1][n+1];
        for (int i =  1 ; i < n+1 ; i++) {
            Arrays.fill(map[i], Integer.MAX_VALUE);
            map[i][i] = 0;
        }
        
        for (int[] fare : fares) {
            map[fare[0]][fare[1]] = fare[2];
            map[fare[1]][fare[0]] = fare[2];
        }
        
        for (int k = 1 ; k < n+1 ; k++) {
            for (int i = 1 ; i < n+1 ; i++) {
                for (int j = 1 ; j < n+1 ; j++) {
                    if (i == j) map[i][j] = 0;
                    else {
                        if (map[i][k] != Integer.MAX_VALUE && map[k][j] != Integer.MAX_VALUE) {
                            map[i][j] = Math.min(map[i][j], map[i][k] + map[k][j]);
                        } 
                    }
                }
            }
        }
        
        int money = Integer.MAX_VALUE;
        
        for (int i = 1 ; i < n+1 ; i++) {
            if (money > map[s][i] + map[i][a] + map[i][b]) {
                money = map[s][i] + map[i][a] + map[i][b];
            }
        }

        return money;
    }
}
