// Q224.cs
// https://programmers.co.kr/learn/courses/30/lessons/12934?language=csharp

using System;

public class Solution
{
    public long solution(long n)
    {
        double num = Math.Sqrt(n);
        long integer = (long)num;
        
        if (integer == num)
        {
            integer ++;
            return integer * integer;
        }
        return -1;
    }
}