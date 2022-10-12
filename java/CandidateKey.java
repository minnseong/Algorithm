// Programmers 10/12 2022
// Java 코테 연습 - 후보키

package java;
import java.util.*;

class Solution {
    
    private boolean isUnique(List<Integer> list, int now) {
        for (int i = 0 ; i < list.size() ; i++) {
            if ((list.get(i) & now) == list.get(i))
                return false;
        }
        return true;
    }
    
    public int solution(String[][] relation) {
        
        int n = relation.length;
        int m = relation[0].length;
    
        ArrayList<Integer> result = new ArrayList<>();
        
        for (int i = 0 ; i < 1<<m ; i++) {
            HashSet<String> set = new HashSet<String>();
            
            for (int j = 0 ; j < n ; j++) {
                String now = "";
                for (int k = 0 ; k < m ; k++) {
                    if ((i & 1<<k) != 0)
                        now += relation[j][k];
                }
                set.add(now);
            }
            if (set.size() == n && isUnique(result, i)) {
                result.add(i);
            }
        }
        
        return result.size();
    }
}