// Q230.cs
// https://programmers.co.kr/learn/courses/30/lessons/12931?language=csharp

using System;

public class Solution
{
    public int solution(int n)
    {
        char[] num_array = n.ToString().ToCharArray();
        int sum = 0;
        
        for(int i = 0; i < num_array.Length; i++)
            sum += int.Parse(num_array[i].ToString());
        
        return sum;
    }
}