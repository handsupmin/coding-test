// Q221.cs
// https://programmers.co.kr/learn/courses/30/lessons/12940?language=csharp

public class Solution
{
    public int[] solution(int n, int m)
    {
        int[] answer = new int[2];
        int bigger = (n >= m) ? n : m;
        int smaller = (n == bigger) ? m : n;
        int gcd = smaller;
        
        for(int i = gcd; i > 0; i--)
            if(bigger % i == 0 && smaller % i == 0)
            {
                gcd = i;
                break;
            }
        
        int lcm = gcd * (bigger / gcd) * (smaller / gcd);
        
        answer[0] = gcd;
        answer[1] = lcm;
        
        return answer;
    }
}