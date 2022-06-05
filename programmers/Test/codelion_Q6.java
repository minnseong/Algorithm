package programmers.Test;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Scanner;

public class codelion_Q6 {

    public class Post {
        private String title;
        private String content;
    
        public String getTitle() {
            return title;
        }
    
        public void setTitle(String title) {
            this.title = title;
        }
    
        public String getContent() {
            return content;
        }
    
        public void setContent(String content) {
            this.content = content;
        }
    }
        
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Post> board = new ArrayList<>();

        Long cnt = 1L;
        Long listCnt;

        do {
            System.out.print("명령어) ");
            String cmd = sc.nextLine();
            if (Objects.equals(cmd, "등록")) {
                Post post = new Post();
                System.out.print("제목 : ");
                post.setTitle(sc.nextLine());
                System.out.print("내용 : ");
                post.setContent(sc.nextLine());
                System.out.println("[알림] " + (cnt++) +"번글이 등록되었습니다.");
                board.add(post);
            } else if (Objects.equals(cmd, "목록")) {
                System.out.println("번호 / 제목\n-------------------");
                listCnt = cnt;
                for (Post post : board) {
                    System.out.println((--listCnt) + " / " + post.getTitle());
                }

            } else if (Objects.equals(cmd, "종료")) {
                System.out.println("프로그램을 종료합니다.");
                break;
            }
        } while (true);

    }
    
}
