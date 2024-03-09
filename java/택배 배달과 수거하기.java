class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;
        int togoDist = n-1;
        while (true) {
            int deliverDist = -1;
            int pickupDist = -1;
            
            for (int i = togoDist ; i > -1 ; i--) {
                if (deliveries[i] >= 1) {
                    deliverDist = i;
                    break;
                }
            }
            
            for (int i = togoDist ; i > -1 ; i--) {
                if (pickups[i] >= 1) {
                    pickupDist = i;
                    break;
                }
            }
            
        
            if (deliverDist == -1 && pickupDist == -1) {
                break;
            }
            
            togoDist = deliverDist;
            if (togoDist < pickupDist) {
                togoDist = pickupDist;
            }
            
            answer += ((togoDist+1)*2);
            
            int boxCnt = cap;
            for (int i = deliverDist ; i > -1 ; i--) {
                if (deliveries[i] <= boxCnt) {
                    boxCnt -= deliveries[i];
                    deliveries[i] = 0;
                }
                else {
                    deliveries[i] -= boxCnt;
                    break;
                }
            }
            
            boxCnt = cap;
            for (int i = pickupDist ; i > -1 ; i--) {
                if (pickups[i] <= boxCnt) {
                    boxCnt -= pickups[i];
                    pickups[i] = 0;
                }
                else {
                    pickups[i] -= boxCnt;
                    break;
                }
            }
        }
        
        return answer;
    }
}
