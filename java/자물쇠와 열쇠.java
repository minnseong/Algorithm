import java.util.*;

class Solution {
    public boolean solution(int[][] key, int[][] lock) {
        boolean answer = true;
        
        int[][] llock = new int[lock.length * 3][lock.length * 3];

        int cnt = 0;
        for (int i = 0 ; i < lock.length ; i++) {
            for (int j = 0 ; j < lock[0].length ; j++) {
                if (lock[i][j] == 1) {
                    llock[i+lock.length][j+lock.length] = 1;
                } else {
                    cnt += 1;
                }
            }
        }
        
        for (int c = 0 ; c < 4 ; c ++) {
            key = rotate(key);
            for (int i = 0 ; i < llock.length - key.length + 1 ; i++) {
                for (int j = 0 ; j < llock.length - key.length + 1 ; j++) {

                    int success = 0;
                    int fail = 0;
                    for (int m = 0 ; m < key.length ; m++) {
                        for (int n = 0 ; n < key.length ; n++) {
                            if ((i+m) >= lock.length && (i+m) < (lock.length * 2) && (j+n) >= lock.length && (j+n) < (lock.length * 2)) {
                                if (llock[i+m][j+n] == 0 && key[m][n] == 1) {
                                    success += 1;
                                }
                                else if (llock[i+m][j+m] == 1 && key[m][n] == 1) {
                                    fail += 1;
                                }
                            }
                        }
                    }

                    if (fail == 0 && success == cnt) {
                        return true;
                    }
                }
            }
        }
        
        return false;
    }
    
    public static int[][] rotate(int[][] board) {
        
        int[][] tmp = new int[board.length][board[0].length];
        
        for (int i = 0 ; i < board[0].length ; i++) {
            for (int j = 0 ; j < board.length ; j++) {
                tmp[i][j] = board[board.length - j - 1][i];
            }
        }
        
        return tmp;
    }
}
