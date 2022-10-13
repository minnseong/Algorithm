// 신한카드 코딩테스트 10/13 2022
// Q1

package programmers.Test;
import java.util.*;

public class ShinhanCard_Q1 {

    class Solution {
        public int solution(int[] arr) {
            int answer = -1;
            int diff = 1001;

            int threadhold = 0;
            int arrLength = arr.length;

            Arrays.sort(arr);

            HashSet<Integer> set = new HashSet<>();
            set.add(0);

            for (int n : arr) {
                set.add(n);
                if (n+1 <= 255)
                    set.add(n+1);
                if (n-1 >= 0)
                    set.add(n-1);
            }

            for (Integer n : set) {
                int a = Arrays.binarySearch(arr, n);
                if (a < 0)
                    a = (-1) * a - 1;
                int b = arrLength - a;
                if (Math.abs(a-b) < diff) {
                    answer = n;
                    diff = Math.abs(a-b);
                }
                else if (Math.abs(a-b) == diff) {
                    if (n < answer) {
                        answer = n;
                    }
                }
            }

            return answer;
        }
    }
}
