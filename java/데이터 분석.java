import java.util.*;

class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {

        int[][] filteredData = filter(data, ext, val_ext);
        return sort(filteredData, sort_by);
    }
    
    public int[][] sort(int[][] data, String sort_by) {
        
        int idx = getIndex(sort_by);
        Arrays.sort(data, (o1, o2) -> {
            return o1[idx] - o2[idx];
        });
            
        return data;
    }
    
    public int[][] filter(int[][] data, String ext, int val_ext) {
        
        int cnt = 0;
        int extIdx = getIndex(ext);
        
        for (int[] d : data) {
            if (d[extIdx] < val_ext) {
                cnt += 1;
            }
        }
        
        int[][] ret = new int[cnt][];
        int i = 0;
        for (int[] d : data) {
            if (d[extIdx] < val_ext) {
                ret[i] = d;
                i += 1;
            }
        }
        
        return ret;
    }
    
    public int getIndex(String s) {
        if (s.equals("code")) {
            return 0;
        }
        else if (s.equals("date")) {
            return 1;
        }
        else if (s.equals("maximum")) {
            return 2;
        }
        else {
            return 3;
        }
    }
}
