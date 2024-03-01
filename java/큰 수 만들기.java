import java.util.*;

class Solution {
    public String solution(String number, int k) {
        
        Stack<String> stack = new Stack<>();
        String[] nums = number.split("");
        
        for (int i = 0; i < number.length() ; i++) {
            String s = nums[i];
            
            while(!stack.isEmpty() && Integer.parseInt(stack.peek()) < Integer.parseInt(s) && k > 0) {
                stack.pop();
                k -= 1;
            }
            stack.push(s);
        }
        
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        
        return sb.reverse().toString().substring(0, sb.length()-k);
    }
}

/* 시간 초과 코드 
String answer = "";

String[] nums = number.split("");
int numeberLenghth = number.length();
boolean[] remove_idx = new boolean[number.length()];
int removeCnt = 0;

for (int i = 0 ; i < numeberLenghth ; i++) {
    
    if (k == 0) {
        break;
    }
    
    if (remove_idx[i] == true || nums[i] == "9") {
        continue;
    }
    
    int tmpRemoveCnt = 0;
    for (int j = 1 ; j < k-removeCnt+1 ; j++) {
        
        if (i+j < numeberLenghth) {
            if (Integer.parseInt(nums[i]) < Integer.parseInt(nums[i+j])) {
                System.out.println(nums[i] + " " + nums[i+j]);
                tmpRemoveCnt += 1;
                remove_idx[i] = true;
                break;
            }
            else {
                tmpRemoveCnt += 1;
            }
        }
    }
    
    if (remove_idx[i] == true) {
        for (int z = i ; z < i+tmpRemoveCnt ; z++) {
            remove_idx[z] = true;
        }
        k -= tmpRemoveCnt;
    }
}

int lastIdx = numeberLenghth - 1;
while (k > 0) {
    if (remove_idx[lastIdx] == false) {
        remove_idx[lastIdx] = true;
        lastIdx -= 1;
        k -= 1;
    }
}

StringBuilder sb = new StringBuilder();

for (int i = 0 ; i < numeberLenghth ; i++) {
    if (remove_idx[i] == false) {
        sb.append(nums[i]);
    }
}
return sb.toString();
*/
