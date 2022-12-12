class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        String[] a = new String[quiz.length];
        
        for (int i = 0; i < quiz.length; i++) {
            a = quiz[i].split(" ");
            if (a[1].equals("+")) {
                if (Integer.parseInt(a[0]) + Integer.parseInt(a[2]) == Integer.parseInt(a[4])) {
                    answer[i] = "O";
                } else {
                    answer[i] = "X";
                }
            }
            if (a[1].equals("-")) {
                if (Integer.parseInt(a[0]) - Integer.parseInt(a[2]) == Integer.parseInt(a[4])) {
                    answer[i] = "O";
                } else {
                    answer[i] = "X";
                }
            }
        }
        return answer;
    }
}