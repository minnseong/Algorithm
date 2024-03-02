import java.util.*;

class Solution {
    
    static boolean[] visited;
    static String[][] _tickets;
    static List<String> answers = new ArrayList<>();
    
    public String[] solution(String[][] tickets) {
        
        _tickets = tickets;
        visited = new boolean[tickets.length];
        
        dfs("ICN", "ICN", 0);
        Collections.sort(answers);
        
        return answers.get(0).split(" ");
    }
    
    public static void dfs(String routes, String cursor, int useCnt) {
        
        if (useCnt == _tickets.length) {
            answers.add(routes);
            return;
        }
        
        for (int i = 0 ; i < _tickets.length ; i++) {
            if (!visited[i] && _tickets[i][0].equals(cursor)) {
                visited[i] = true;
                dfs(routes + " "  + _tickets[i][1], _tickets[i][1], useCnt+1);
                visited[i] = false;
            }
        }
    }
}
