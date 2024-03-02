class Solution {

    static int[] arr;
    static int answer = 0;
    static int _target;
    static int[] _numbers;
    
    public int solution(int[] numbers, int target) {
        
        arr = new int[numbers.length];
        _target = target;
        _numbers = numbers;
           
        dfs(0);
        return answer;
    }
    
    public void dfs(int depth) {
        
        if (depth == _numbers.length) {
            int tmp = 0;
            for (int i = 0 ; i < _numbers.length ; i++) {
                tmp += arr[i] * _numbers[i];
            }
            if (tmp == _target) {
                answer += 1;
            }
            return;
        }
        
        else {
            arr[depth] = (-1);
            dfs(depth+1);
            arr[depth] = 1;
            dfs(depth+1);
        }   
    }
}
