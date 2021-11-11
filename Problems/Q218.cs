// Q218.cs
// https://programmers.co.kr/learn/courses/30/lessons/12947?language=csharp

using System;

public class Solution
{
    public bool solution(int x)
    {
        bool answer = true;
        string num_to_string = Convert.ToString(x);
        int sum = 0;        
        
        foreach(char char_num in num_to_string)
        {
            sum += Convert.ToInt32(char_num.ToString());
        }
        
        if (x % sum == 0)
            answer = true;
        else
            answer = false;
        
        return answer;
    }
}