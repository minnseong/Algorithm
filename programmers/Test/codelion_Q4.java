package programmers.Test;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class codelion_Q4 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        List<Integer> numberList = new ArrayList<>();

        Long cnt = 1L;
        int input = -1;

        System.out.println("0을 입력하시면 입력이 종료 됩니다.");
        while (input != 0) {
            System.out.print("숫자 " + (cnt++) + " : ");
            try {
                input = Integer.parseInt(sc.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("[입력오류] : 숫자로 입력해주세요.");
                cnt--;
                continue;
            }
            if (input != 0)
                numberList.add(input);
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
}
