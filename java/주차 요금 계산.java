import java.util.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        
        int basicTime = fees[0];
        int basicFee = fees[1];
        int degreeTime = fees[2];
        int degreeFee = fees[3];
        
        Map<String, List<Integer>> rcds = new HashMap<>();
        
        for (String record : records) {
            String[] rcd = record.split(" ");
            
            if (!rcds.containsKey(rcd[1])) {
                rcds.put(rcd[1], new ArrayList<>());
            }
            
            rcds.get(rcd[1]).add(toMinute(rcd[0]));
        }
        
        List<String> keys = new ArrayList<>(rcds.keySet());
        Collections.sort(keys, (o1, o2) -> {
            return Integer.valueOf(o1) - Integer.valueOf(o2);
        });
        
        int[] answer = new int[keys.size()];
        int idx = 0;
        for (String key : keys) {
            Integer timeSum = 0;
            for (int i = 0 ; i < rcds.get(key).size() ; i++) {
                if (i % 2 == 0) timeSum -= rcds.get(key).get(i);
                else timeSum += rcds.get(key).get(i);
            }
            
            if (rcds.get(key).size() % 2 == 1) {
                timeSum += toMinute("23:59");
            }
            
            if (timeSum <= basicTime) {
                answer[idx] = basicFee;
            } else {
                answer[idx] = basicFee;
                
                int overTime = timeSum - basicTime;
                answer[idx] += (Math.ceil(overTime / (float) degreeTime) * degreeFee);
            }
            idx += 1;
        }
        
        
        return answer;
    }
    
    public static Integer toMinute(String time) {
        String[] t = time.split(":");
        
        return Integer.valueOf(t[0]) * 60 + Integer.valueOf(t[1]);
    }
}
