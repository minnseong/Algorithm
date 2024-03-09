import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        
        Map<String, Integer> hist = new HashMap<>();
        Map<String, int[]> frds = new HashMap<>();
        
        for (String fd : friends) {
            frds.put(fd, new int[] {0, 0, 0});
        }
        
        for (String gift : gifts) {
            hist.put(gift, hist.getOrDefault(gift, 0)+1);
            String[] fds = gift.split(" ");
            frds.get(fds[0])[0] += 1;
            frds.get(fds[1])[1] += 1;
        }
        
        Set<String> visited = new HashSet<>();
        
        for (String f1 : friends) {
            for (String f2: friends) {
                if (!f1.equals(f2) && !visited.contains(f1 + " " + f2)) {
                    String w1 = f1 + " " + f2;
                    String w2 = f2 + " " + f1;

                    if (hist.getOrDefault(w1, 0) > hist.getOrDefault(w2, 0)) {
                        frds.get(f1)[2] += 1;
                    } else if (hist.getOrDefault(w1, 0) < hist.getOrDefault(w2, 0)) {
                        frds.get(f2)[2] += 1;
                    } else {
                        if ((frds.get(f2)[0] - frds.get(f2)[1]) > (frds.get(f1)[0] - frds.get(f1)[1])) {
                            frds.get(f2)[2] += 1;
                        } else if ((frds.get(f2)[0] - frds.get(f2)[1]) < (frds.get(f1)[0] - frds.get(f1)[1])) {
                            frds.get(f1)[2] += 1;
                        }
                    }

                    visited.add(w1);
                    visited.add(w2);
                }
            }
        }
        
        for (String friend : friends) {
            if (answer < frds.get(friend)[2]) {
                answer = frds.get(friend)[2];
            }
        }
        
        return answer;
    }
}
