class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        
        Integer posSecond = convertSecondFrom(pos);
        Integer videoLenSecond = convertSecondFrom(video_len);
        Integer opStartSecond = convertSecondFrom(op_start);
        Integer opEndSecond = convertSecondFrom(op_end);
        
        if (posSecond >= opStartSecond && posSecond <= opEndSecond) {
            posSecond = opEndSecond;
        }
        
        for (String command : commands) {
            if ("next".equals(command)) {
                Integer posSecondTmp = posSecond + 10;
                
                if (posSecondTmp >= videoLenSecond) {
                    posSecond = videoLenSecond;
                }
                else {
                    posSecond = posSecondTmp;
                }
            }
            if ("prev".equals(command)) {
                Integer posSecondTmp = posSecond - 10;
             
                if (posSecondTmp <= 0) {
                    posSecond = 0;
                }
                else {
                    posSecond = posSecondTmp;
                }
            }
            
            if (posSecond >= opStartSecond && posSecond <= opEndSecond) {
                posSecond = opEndSecond;
            }
        }
        
        return convertTimeFrom(posSecond);
    }
    
    private Integer convertSecondFrom(String time) {
        String[] t = time.split(":");
        return Integer.valueOf(t[0]) * 60 + Integer.valueOf(t[1]);
    }
    
    private String convertTimeFrom(Integer second) {
        
        String time = "";
        
        if (second / 60 < 10) {
            time += "0";
        }
        
        time += String.valueOf(second / 60);
        time += ":";
        
        if (second % 60 < 10) {
            time += "0";
        }
        
        time += String.valueOf(second % 60);
        
        return time;
    }
}
