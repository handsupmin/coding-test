// Q220.cs
// https://programmers.co.kr/learn/courses/30/lessons/12943

public class Solution
{
    public int solution(long num)
    {
        int count = 0;
        
        while(count < 500)
        {
            if(num == 1)
                break;            
            else if(num % 2 == 0)
                num /= 2;
            else
                num = num * 3 + 1;
            
            count += 1;
        }
        
        if(count == 500)
            return -1;
        
        return count;
    }
}