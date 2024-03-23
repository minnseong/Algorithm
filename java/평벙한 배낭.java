import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();   // 물건 개수
        int k = sc.nextInt();   // 가방 크기

        int[][] items = new int[n+1][2];

        for(int i = 1 ; i < n+1 ; i ++) {
            items[i] = new int[] {sc.nextInt(), sc.nextInt()};
        }

        int[][] dp = new int[n+1][k+1];

        for (int i = 1 ; i < n+1 ; i++) {
            for (int j = 1 ; j < k+1 ; j++) {

                dp[i][j] = dp[i-1][j];

                if (j-items[i][0] >= 0) {
                    dp[i][j] = Math.max(dp[i][j], dp[i-1][j-items[i][0]]+items[i][1]);
                }
            }
        }

        System.out.println(dp[n][k]);
    }
}
