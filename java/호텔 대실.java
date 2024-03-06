import java.util.*;

class Solution {
    public int solution(String[][] book_time) {
        int answer = 0;
        
        int[][] books = new int[book_time.length][2];
        
        for (int i = 0 ; i < book_time.length ; i++) {
            books[i][0] = toTime(book_time[i][0]);
            books[i][1] = toTime(book_time[i][1]) + 10;
        }
        
        int lt = 60*23 + 59;
        for (int i = 0 ; i < lt ; i++) {
            int cnt = 0;
            for (int[] b : books) {
                if (b[0] <= i && i < b[1]) {
                    cnt += 1;
                }
            }
            
            if (cnt > answer) {
                answer = cnt;
            }
        }
        
        return answer;
    }
    
    public static int toTime(String time) {
        
        String[] t = time.split(":");
        int hour = Integer.valueOf(t[0]);
        int minute = Integer.valueOf(t[1]);
        
        return (hour * 60) + minute;
    }
}
