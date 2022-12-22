// Programmers 12/22 2022
// Java 코테 연습 - 가장 가까운 같은 글자

package java;

import java.util.*;

public class NearestSameLetter {
    class Solution {
        public int[] solution(String s) {
            int[] answer = new int[s.length()];
        
            Map<Character, Integer> map = new HashMap<>();
            
            for (Integer i = 0 ; i < s.length() ; i++) {
                if (map.containsKey(s.charAt(i))) {
                    answer[i] = i - map.get(s.charAt(i));
                    map.put(s.charAt(i), i);
                }
                else {
                    answer[i] = -1;
                    map.put(s.charAt(i), i);
                }
            }
            
            
            return answer;
        }
    }
}
