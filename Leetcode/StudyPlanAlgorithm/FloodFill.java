// LeetCode 2021 . 12 . 19
// Study Plan - Algorithm Day 7 733. Flood Fill
package Leetcode.StudyPlanAlgorithm;

import java.util.Arrays;

class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int m = image[0].length;
        int n = image.length;
        int color = image[sr][sc];
        int [] stack = new int[10];
        
        boolean [][] visited = new boolean[m][n];
        for(boolean a[] :visited) {
            Arrays.fill(a, false);
        }
        
        while(true) {
            int x = 1;
            int y = 2;
            int [][] dir = {{x+1, y}, {x, y+1}, {x-1, y}, {x, y-1}};

            for (int d[] : dir) {
                if(!visited[d[0]][d[1]] && image[d[0]][d[1]] == color) {
                
                }
            }
        }
    }
    
   
}