import java.util.*;

class Solution {
    public int solution(int N, int[][] road, int K) {
        int answer = 0;

        Map<Integer, List<Integer[]>> graph = new HashMap<>();
        for (int i = 1 ; i <= N ; i++) {
            graph.put(i, new ArrayList<>());
        }
        
        for (int[] r : road) {
            graph.get(r[0]).add(new Integer[] {r[1], r[2]});
            graph.get(r[1]).add(new Integer[] {r[0], r[2]});
        }
        
        PriorityQueue<Integer[]> pq = new PriorityQueue<>((o1, o2) -> (o1[1]-o2[1]));
        int[] dists = new int[N+1];
        Arrays.fill(dists, Integer.MAX_VALUE);
        dists[1] = 0;
        pq.add(new Integer[] {1, 0});
        
        while(!pq.isEmpty()) {
            Integer[] now = pq.poll();
            
            if (dists[now[0]] < now[1]) {
                continue;
            }
            
            for (Integer[] next : graph.get(now[0])) {
                if (dists[next[0]] > (now[1] + next[1])) {
                    dists[next[0]] = (now[1] + next[1]);
                    pq.add(new Integer[] {next[0], (now[1] + next[1])});
                }
            }
        }
        
        for (int i = 1 ; i <= N ; i++) {
            if (dists[i] <= K) {
                answer += 1;
            }
        }

        return answer;
    }
}
