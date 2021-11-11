// Q214.cs
// https://programmers.co.kr/learn/courses/30/lessons/12954?language=csharp

public class Solution
{
    public long[] solution(int x, int n)
    {
        long[] answer = new long[n];
        
        for(long i = 0; i < n; i++) {
            answer[i] = x * (i + 1);
        }
        
        return answer;
    }
}