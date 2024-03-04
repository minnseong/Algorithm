import java.util.*;

class Solution {
    
    static String[] nums;
    static boolean[] bfsVisited;
    static Set<String> set;
    
    public int solution(String numbers) {
        int answer = 0;
        
        boolean[] visited = new boolean[10];
        visited[0] = true;
        
        nums = numbers.split("");
        set = new HashSet<>();
        
        for (int i = 0 ; i < nums.length ; i++) {
            if (isPrime(Integer.valueOf(nums[i]))) {
                set.add(nums[i]);
            }
        }
        for (int i = 0 ; i < nums.length ; i++) {
            if (!visited[Integer.valueOf(nums[i])]) {
                bfsVisited = new boolean[numbers.length()];
                bfsVisited[i] = true;
                visited[Integer.valueOf(nums[i])] = true;
                bfs(nums[i]);
            }
        }
        
        return set.size();
    }
    
    public static void bfs(String nm) {
        
        for (int i = 0 ; i < bfsVisited.length ; i++) {
            if (!bfsVisited[i]) {
                
                nm = nm + nums[i];
                bfsVisited[i] = true;
                if (isPrime(Integer.valueOf(nm))) {
                    set.add(nm);
                }
                bfs(nm);
                bfsVisited[i] = false;
                nm = nm.substring(0, nm.length()-1);
            }
            
        }
    }
    
    public static boolean isPrime(Integer n) {
        
        if (n < 2) return false;
        if (n == 2) return true;
        
        for (int i = 2 ; i <= (n / 2) + 1 ; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
