import java.util.*;

class Solution {
    
    public String solution(String play_time, String adv_time, String[] logs) {
        
        int playTime = toSecond(play_time);
        int advTime = toSecond(adv_time);
        
        long[] arr = new long[playTime+1];
        
        for (String log : logs) {
            
            String[] time = log.split("-");
            
            Integer st = toSecond(time[0]);
            Integer et = toSecond(time[1]);
            
            arr[st] += 1;
            arr[et] -= 1; 
        }
        
        for (int i = 1 ; i < arr.length ; i++) {
            arr[i] += arr[i-1];
        }
        
        long total = 0;
        for (int i = 1 ; i <= advTime ; i++) {
            total += arr[i];
        } 
        
        int answer = 0;
        int j = 1;
        long ansTotal = total;
        for (int i = advTime + 1 ; i <= playTime ; i++) {
            total = total - arr[j] + arr[i];
            if (ansTotal < total) {
                answer = j+1;
                ansTotal = total;
            }
            j+=1;
        }
        System.out.println(toTime(ansTotal));
        return toTime(answer);
    }
    
    public static Integer toSecond(String time) {
        
        String[] t = time.split(":");
        
        return Integer.valueOf(t[0]) * 3600 + Integer.valueOf(t[1]) * 60 + Integer.valueOf(t[2]);
    }
    
    public static String toTime(long time) {
        StringBuilder sb = new StringBuilder();
        
        if (String.valueOf(time/3600).length() == 1) {
            sb.append("0");
        }
        sb.append(String.valueOf(time/3600));
        sb.append(":");
        if (String.valueOf(time%3600/60).length() == 1) {
            sb.append("0");
        }
        sb.append(String.valueOf(time%3600/60));
        sb.append(":");
        if (String.valueOf(time%3600%60).length() == 1) {
            sb.append("0");
        }
        sb.append(String.valueOf(time%3600%60));
        
        return sb.toString();
    }
}    
