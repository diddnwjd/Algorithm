import java.util.Arrays;

class Solution {
    public int solution(int[] array) {
        Arrays.sort(array);
        int size = array.length;
        int answer = size / 2;
        return array[answer];
    }
}