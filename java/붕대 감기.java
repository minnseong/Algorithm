import java.util.*;

class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;
    
        int[] time = new int[attacks[attacks.length-1][0]+1];
        int maxHealth = health;
        
        for (int[] attack : attacks) {
            time[attack[0]] = -attack[1];
        }
        
        for (int i = 1 ; i < attacks[attacks.length-1][0]+1 ; i++) {
            if (time[i] < 0) {
                continue;
            }
            
            if (time[i-1] != bandage[0] && time[i-1] >= 0) {
                time[i] = time[i-1] + 1;
            } else {
                time[i] = 1;         
            }
        }
        
        for (int i = 0 ; i < attacks[attacks.length-1][0]+1 ; i++) {
            if (time[i] < 0) {
                health += time[i];
                
                if (health <= 0) {
                    return -1;
                }
            } else {
                if (time[i] == bandage[0]) {
                    health += bandage[2];
                    health += bandage[1];
                } else {
                    health += bandage[1];
                }
                
                if (health > maxHealth) {
                    health = maxHealth;
                }
            }
            
            
        }
        
        return health;
    }
}
