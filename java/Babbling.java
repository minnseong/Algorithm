// Programmers 10/10 2022
// Java 코테 연습 - 옹알이

package java;

public class Babbling {
    class Solution {
        public int solution(String[] babbling) {
            int answer = 0;
    
            String[] pron = {"aya", "ye", "woo", "ma"};
    
            for (String b : babbling) {
    
                int i = 0;
                int cnt = 0;
                String prev = "";
                boolean flag = false;
                while (i < b.length()) {
                    for (String p : pron) {
                        if (i+p.length() <= b.length() && b.substring(i, i+p.length()).equals(p)) {
                            if (p == prev) {
                                flag = true;
                                break;
                            }
                            if (i+p.length() == b.length()) {
                                answer += 1;
                                flag = true;
                                break;
                            }
                            i += p.length();
                            prev = p;
                            cnt = 0;
                            break;
                        }
                        cnt += 1;
                    }
                    if (cnt == 4 || flag == true) {
                        cnt = 0;
                        break;
                    }
                }
            }
            return answer;
        }
    }
}
