import java.util.*;

class Solution {
    
    public int solution(int N, int number) {
        int answer = 0;
        Map<Integer, Set<Integer>> map = new HashMap<>();
        
        for (int i = 1 ; i < 9 ; i++) {
            map.put(i, new HashSet<Integer>());
            map.get(i).add(getNextNumber(N, i));
        }
        
        for (int i = 2 ; i < 9 ; i++) {
            for (int j = 1 ; j < i ; j++) {
                for (Integer a : map.get(j)) {
                    for (Integer b : map.get(i-j)) {
                        map.get(i).add(a + b);
                        map.get(i).add(a - b);
                        map.get(i).add(a * b);
                        if (b != 0) {
                            map.get(i).add(a / b);
                        }
                    }
                }
                
            }
        }
        
        for (int i = 1 ; i < 9 ; i++) {
            if (map.get(i).contains(number)) {
                return i;
            }
        }
        
        return -1;
    }
    
    public static int getNextNumber(int number, int cnt) {
        
        int res = number;
        
        for (int i = 1 ; i < cnt ; i++) {
            res = (10 * res) + number;
        }
        return res;
    }
}
