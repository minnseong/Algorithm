import java.util.*;

class Solution {
    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
        
        int[] answer = new int[] {0 , Integer.MAX_VALUE};
        Set<Integer> gateSet = new HashSet<>();
        Set<Integer> summitSet = new HashSet<>();
        
        for (int gate : gates) gateSet.add(gate);        
        for (int summit : summits) summitSet.add(summit);
        
        Map<Integer, List<Integer[]>> graph = new HashMap<>();
        for (int i = 1 ; i <= n ; i++) {
            graph.put(i, new ArrayList<>());
        }
        
        for (int[] path : paths) {
            graph.get(path[0]).add(new Integer[] {path[1], path[2]});
            graph.get(path[1]).add(new Integer[] {path[0], path[2]});
        }
        
        PriorityQueue<Integer[]> pq = new PriorityQueue<>(
            (o1, o2) -> (o1[1] - o2[1])
        );
        
        int[] intensities = new int[n+1];
        Arrays.fill(intensities, Integer.MAX_VALUE);
        for (int gate : gates) {
            pq.add(new Integer[] {gate, 0});
            intensities[gate] = 0;
        }
        
        while (!pq.isEmpty()) {
            
            Integer[] now = pq.poll();
            
            if (summitSet.contains(now[0]) || now[1] > intensities[now[0]]) {
                continue;
            }
            
            for (Integer[] next : graph.get(now[0])) {
                
                if (!gateSet.contains(next[0])) {
                    int its = Math.max(now[1], next[1]);
                    if (intensities[next[0]] > its) {
                        intensities[next[0]] = its;
                        pq.add(new Integer[] {next[0], its});
                    }
                }
            }
        }
        
        Arrays.sort(summits);
        for (int summit : summits) {
            if (answer[1] > intensities[summit]) {
                answer[0] = summit;
                answer[1] = intensities[summit];
            }
        }
        
        return answer;
    }
}
