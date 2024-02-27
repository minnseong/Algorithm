import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        
        Arrays.sort(jobs, (o1, o2) -> o1[0] - o2[0]);
        PriorityQueue<int[]> queue = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);
        
        int task_idx = 0;
        int finish_task = 0;
        int start_time = 0;
        
        while (true) {
            if (finish_task == jobs.length) { break; }
            
            while (task_idx < jobs.length && start_time >= jobs[task_idx][0]) {
                queue.add(jobs[task_idx]);
                task_idx++;
            }
            
            if (queue.isEmpty() && task_idx < jobs.length) {
                start_time = jobs[task_idx][0];
            } else {
                int[] job = queue.poll();
                answer += (start_time + job[1] - job[0]);
                start_time = start_time + job[1];
                finish_task++;
            }
        }
    
        return answer / jobs.length;
    }
}
