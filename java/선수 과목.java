import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 과목 수
        int M = Integer.parseInt(st.nextToken()); // 선수 조건 수

        int[] indegree = new int[N+1];
        Map<Integer, ArrayList<Integer>> map = new HashMap<>();

        for (int i = 0 ; i < N+1 ; i++) {
            map.put(i, new ArrayList<>());
        }

        for(int i=0;i<M;i++) {
            st = new StringTokenizer(br.readLine());
            int pre = Integer.parseInt(st.nextToken());
            int next = Integer.parseInt(st.nextToken());

            indegree[next] += 1;
            map.get(pre).add(next);
        }

        Queue<Integer[]> queue = new LinkedList<>();
        int[] result = new int[N];

        for (int i = 1 ; i < N+1 ; i++) {
            if (indegree[i] == 0) {
                queue.add(new Integer[] {i, 1});
            }
        }

        while (!queue.isEmpty()) {
            Integer[] now = queue.poll();

            result[now[0]-1] = now[1];

            for (Integer next : map.get(now[0])) {
                indegree[next] -= 1;
                if (indegree[next] == 0) {
                    result[next - 1] = now[1] + 1;
                    queue.add(new Integer[]{next, now[1] + 1});
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (Integer i : result) {
            sb.append(i).append(' ');
        }

        System.out.println(sb);
    }
}
