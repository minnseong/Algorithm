import java.util.*;

class Solution {
    public int solution(int n, int[] money) {
        int answer = 0;
        
        Arrays.sort(money);
        int[] m = new int[n+1];
        
        for (int mn : money) {
            m[mn] = m[mn] + 1;
            for (int i = mn + 1 ; i < n+1 ; i++ ) {
                m[i] = m[i-mn] + m[i];
            }
        }
        
        return m[n] % 1000000007;
    }
}
