import java.util.*;

class Solution {
    
    static int[][] dir = {
        {0, 1}, {1, 0}, {-1, 0}, {0, -1}
    };
    
    public int[] solution(String[][] places) {
        int[] answer = new int[places.length];
        
        for (int i = 0 ; i < places.length ; i++) {
            String[][] board = new String[5][5];
            
            for (int j = 0 ; j < 5 ; j++) {
                board[j] = places[i][j].split("");
            }
            
            int ans = 1;
            for (int m = 0 ; m < 5 ; m++) {
                for (int n = 0 ; n < 5 ; n++) {
                    if (board[m][n].equals("P")) {
                        if (check(board, m, n)) {
                            ans = 0;
                        }
                    }
                }
            }
            answer[i] = ans;
        }
        
        
        return answer;
    }
    
    public static boolean isClose(int x, int y, int x1, int y1) {
        if (Math.abs(x-x1) + Math.abs(y-y1) <= 2) {
            return true;
        }
        return false;
    }
    
    public static boolean check(String[][] places, int x, int y) {
        
        Queue<Integer[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[places.length][places[0].length];
        
        queue.add(new Integer[] {x, y});
        visited[x][y] = true;
        
        while (!queue.isEmpty()) {
            
            Integer[] now = queue.poll();
            
            for (int[] d : dir) {
                int dx = now[0] + d[0];
                int dy = now[1] + d[1];
                
                if (0 > dx || dx >= places.length || 0 > dy || dy >= places[0].length) continue;
                if (visited[dx][dy] || !isClose(x, y, dx, dy) || places[dx][dy].equals("X")) continue;
                
                if (places[dx][dy].equals("O")) {
                    queue.add(new Integer[] {dx, dy});
                    visited[dx][dy] = true;
                } else if (places[dx][dy].equals("P")) {
                    return true;
                }
            }
        } 
        return false;
    }
}
