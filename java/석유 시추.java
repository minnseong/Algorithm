import java.util.*;

class Solution {
    public int solution(int[][] land) {
        int answer = 0;
        
        int[][] dir = new int[][] {
            {0, -1}, {-1, 0}, {1, 0}, {0, 1}
        };
        
        int[] amount = new int[land[0].length];
        
        boolean[][] visited = new boolean[land.length][land[0].length];
        
        
        for (int i = 0 ; i < land.length ; i++) {
            for (int j = 0 ; j < land[0].length ; j++) {
                if (!visited[i][j] && land[i][j] == 1) {
                    
                    Set<Integer> set = new HashSet<>();
                    Queue<Integer[]> queue = new LinkedList<>();
                    queue.add(new Integer[] {i, j});
                    int sum = 0;
                    set.add(j);
                    visited[i][j] = false;
                    while(!queue.isEmpty()) {
                        
                        Integer[] now = queue.poll();
                        
                        for (int[] d : dir) {
                            int dx = d[0] + now[0];
                            int dy = d[1] + now[1];
                            
                            if (0 <= dx && dx < land.length && 0 <= dy && dy < land[0].length) {
                                if (!visited[dx][dy] && land[dx][dy] == 1) {
                                    set.add(dy);
                                    queue.add(new Integer[] {dx, dy});
                                    visited[dx][dy] = true;
                                    sum += 1;
                                }
                            }
                        }
                    }
                    if (sum == 0) sum = 1;
                     for (Integer d : set) {
                        amount[d] += sum;
                    }   
                }
                
            }
        }
        
        for (int a : amount) {
            if (answer < a) answer = a;
        }
        return answer;
    }
}
