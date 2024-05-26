import java.util.*;

class Solution {
    
    static boolean[] visited;
    static int routeCnt;
    static List<String> answers;
    
    public String[] solution(String[][] tickets) {
        String[] answer = {};
        
        routeCnt = tickets.length;
        visited = new boolean[routeCnt];
        answers = new ArrayList<>();
        
        dfs(tickets, 0, "ICN", "ICN");
    
        Collections.sort(answers);
        
        return answers.get(0).split("-");
    }
    
    private void dfs(String[][] tickets, int depth, String route, String prev) {
        
        if (depth == routeCnt) {
            answers.add(route);
            return;
        }
        
        for (int i = 0 ; i < routeCnt ; i++) {
            if (!visited[i] && tickets[i][0].equals(prev)) {
                visited[i] = true;
                dfs(tickets, depth+1, route+"-"+tickets[i][1], tickets[i][1]);
                visited[i] = false;
            }
        }
        
    }
}
