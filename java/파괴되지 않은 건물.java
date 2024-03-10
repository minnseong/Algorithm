import java.util.*;

class Solution {
    public int solution(int[][] board, int[][] skill) {
        int answer = 0;
        
        int[][] tb = new int[board.length + 1][board[0].length + 1];
        
        for (int[] skl : skill) {
            if (skl[0] == 1) {
                tb[skl[1]][skl[2]] -= skl[5];
                tb[skl[1]][skl[4]+1] += skl[5];
                tb[skl[3]+1][skl[2]] += skl[5];
                tb[skl[3]+1][skl[4]+1] -= skl[5];
            } else {
                tb[skl[1]][skl[2]] += skl[5];
                tb[skl[1]][skl[4]+1] -= skl[5];
                tb[skl[3]+1][skl[2]] -= skl[5];
                tb[skl[3]+1][skl[4]+1] += skl[5];
            }
        }
        
        for (int i = 0 ; i < tb.length ; i++) {
            for (int j = 1 ; j < tb[0].length ; j++) {
                tb[i][j] += tb[i][j-1];
            }
        }
        
        for (int i = 0 ; i < tb[0].length ; i++) {
            for (int j = 1 ; j < tb.length ; j++) {
                tb[j][i] += tb[j-1][i];
            }
        }
        
        for (int i = 0 ; i < board.length ; i++) {
            for (int j = 0 ; j < board[0].length ; j++) {
                if (board[i][j] + tb[i][j] >= 1) {
                    answer += 1;
                }
            }
        }
        return answer;
    }
}
