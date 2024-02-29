import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        
        PriorityQueue<Integer> minQueue = new PriorityQueue<>();
        PriorityQueue<Integer> maxQueue = new PriorityQueue<>(Collections.reverseOrder());
        
        int cnt = 0;
        int min_remove = 0;
        int max_remove = 0;
        
        for (String op : operations) {
            String[] o = op.split(" ");
            
            if (o[0].equals("I")) {
                minQueue.add(Integer.parseInt(o[1]));
                maxQueue.add(Integer.parseInt(o[1]));
                cnt += 1;
            } else if (o[0].equals("D") && o[1].equals("1")) {
                maxQueue.poll();
                if ((max_remove + min_remove) < cnt) {
                    max_remove += 1;
                }
            } else {
                minQueue.poll();
                if ((max_remove + min_remove) < cnt) {
                    min_remove += 1;
                }
            }
            
            if ((min_remove + max_remove) == cnt) {
                maxQueue.clear();
                minQueue.clear();
            }
        }
        
        if (minQueue.size() == 0 && maxQueue.size() == 0) {
            return new int[] {0, 0};
        }
        
        return new int[] {maxQueue.peek(), minQueue.peek()};
    }
}
