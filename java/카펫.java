import java.util.*;

class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        List<Integer> list = new ArrayList<>();
        
        for (int i = 1 ; i <= yellow + 1 ; i++) {
            if (yellow % i == 0) {
                list.add(i);
            }
        }
        
        for (Integer l : list) {
            if (brown == (l*2 + (yellow/l)*2 + 4)) {
                if ((l + 2) > (yellow / l + 2)) {
                    answer[0] = (l + 2);
                    answer[1] = (yellow / l + 2);
                }
                else {
                    answer[0] = (yellow / l + 2);
                    answer[1] = (l + 2); 
                }
                break;
            }
        }
        
        
        return answer;
    }
}
