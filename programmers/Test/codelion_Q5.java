package programmers.Test;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class codelion_Q5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> numberList = new ArrayList<>();

        long cnt = 1L;
        int input = -1;

        System.out.println("[안내] 0을 입력하시면 입력이 종료 됩니다.");
        while (input != 0) {
            System.out.print("숫자 " + (cnt++) + " : ");
            try {
                input = Integer.parseInt(sc.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("[입력오류] : 숫자로 입력해주세요.");
                cnt--;
                continue;
            }
            if (input != 0) {
                if (isPrime(input)) {
                    if (numberList.contains(input)) {
                        System.out.println("[입력오류] : 이미 입력된 숫자 입니다.");
                        cnt--;
                    }
                    else
                        numberList.add(input);
                }
            }
        }

        System.out.print("결과 : ");
        int len = numberList.size();
        for (Integer num : numberList) {
            if (--len == 0)
                System.out.println(num);
            else
                System.out.print(num + ", ");
        }
    }

    private static boolean isPrime(Integer n) {
        if (n == 1 || n < 0)
            return false;
        for (int i = 2 ; i <= Math.sqrt(n) ; i++)
            if (n % i == 0)
                return false;
        return true;
    }
}
