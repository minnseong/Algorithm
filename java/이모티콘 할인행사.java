import java.util.*;

class Solution {
    
    static Stack<Integer> rates;
    static List<List<Integer>> answers;
    static Integer[] cases = new Integer[] {10, 20, 30, 40};
    
    public int[] solution(int[][] users, int[] emoticons) {
        int[] answer = new int[] {0, 0};
        
        rates = new Stack<Integer>();
        answers = new ArrayList<>();
        
        dfs(users, emoticons);
        
        Collections.sort(answers, (o1, o2) -> {
           if (o1.get(0) == o2.get(0)) {
               return o2.get(1) - o1.get(1);
           } else {
               return o2.get(0) - o1.get(0);
           }
        });
        
        answer[0] = answers.get(0).get(0);
        answer[1] = answers.get(0).get(1);
        return answer;
    }
    
    public static void dfs(int[][] users, int[] emoticons) {
        
        if (rates.size() == emoticons.length) {
            
            List<Integer> ans = new ArrayList<>();
            ans.add(0);
            ans.add(0);
            
            for (int[] user : users) {
                int money = 0;
                for (int i = 0 ; i < emoticons.length ; i++) {
                    if (rates.get(i) >= user[0]) {
                        money += (emoticons[i] * (100-rates.get(i)) / 100);
                    }
                }
                
                if (money >= user[1]) {
                    ans.set(0, ans.get(0)+1);
                } else {
                    ans.set(1, ans.get(1)+money);
                }
            }
            
            answers.add(ans);
            return;
        }
        
        for (Integer r : cases) {
            rates.add(r);
            dfs(users, emoticons);
            rates.pop();   
        }   
    }
}
