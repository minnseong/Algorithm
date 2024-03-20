import java.util.*;

class Solution {
    public String solution(String m, String[] musicinfos) {
        String answer = "";
    
        List<String> mList = getMList(m);
        
        Arrays.sort(musicinfos, (o1, o2) -> {
            int t1 = getTime(o1.split(",")[0], o1.split(",")[1]);
            int t2 = getTime(o2.split(",")[0], o2.split(",")[1]);
            
            return t2-t1;
        });
        
        for (String musicinfo : musicinfos) {
            
            String[] info = musicinfo.split(","); 
            Integer time = getTime(info[0], info[1]);
            
            List<String> iList = getMList(info[3]);
            System.out.println(iList);
            
            Set<String> set = new HashSet<>();
            
            
            for (int i = 0 ; i < time-mList.size()+1 ; i++) {
                StringBuilder sb = new StringBuilder();
                for (int j = 0 ; j < mList.size() ; j++) {
                    sb.append(iList.get((i+j) % iList.size()));
                }
                set.add(sb.toString());
            }
            
            if (set.contains(m)) {
                answer = info[2];
                break;
            }
        }
        
        if (answer.length() == 0) {
            answer = "(None)";
        } 
        return answer;
    }
    
    public static List<String> getMList(String m) {
        List<String> mm = new ArrayList<>();
        
        int i = 0;
        while (i < m.length()-1) {
            if (m.charAt(i+1) == '#') {
                mm.add(m.substring(i, i+2));
                i += 2;
            }
            else {
                mm.add(Character.toString(m.charAt(i)));
                i += 1;
            }
        }
        
        if (m.charAt(m.length()-1) != '#') {
            mm.add(Character.toString(m.charAt(m.length()-1)));
        }
        
        return mm;
    }
    
    public static Integer getTime(String start, String end) {
        
        String[] st = start.split(":");
        String[] et = end.split(":");
        
        return Integer.valueOf(et[0])*60 + Integer.valueOf(et[1]) - Integer.valueOf(st[0]) * 60 - Integer.valueOf(st[1]);
    }
}
