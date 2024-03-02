import java.util.*;

class Solution {
    
    public int solution(int[][] maps) {
        int answer = -1;
        
        int row = maps[0].length;
        int col = maps.length;
        boolean[][] visited = new boolean[col][row];
        
        int[][] dir = {
            {0, 1}, {0, -1}, {-1, 0}, {1, 0}
        };
        
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] {0 ,0, 0});
        
        while(!queue.isEmpty()) {
            
            int[] pos = queue.poll();
            int x = pos[0];
            int y = pos[1];
            int cnt = pos[2];
            
            if (x == col-1 && y == row-1) {
                answer = cnt + 1;
                break;
            }
            
            for (int i = 0 ; i < 4 ; i++) {
                int dx = x + dir[i][0];
                int dy = y + dir[i][1];
                
                if (0 <= dx && dx < col && 0 <= dy && dy < row && maps[dx][dy] == 1) {
                    if (!visited[dx][dy]) {
                        queue.add(new int[] {dx, dy, cnt+1});
                        visited[dx][dy] = true;
                    }
                }
            }
        } 
        
        return answer;
    }
}
