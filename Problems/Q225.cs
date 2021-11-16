// Q225.cs
// https://programmers.co.kr/learn/courses/30/lessons/12933?language=csharp

using System;
using System.Collections;

public class Solution
{
    public long solution(long n)
    {
        string s = Convert.ToString(n);
        ArrayList a = new ArrayList();
        
        foreach(char i in s)
        {
            a.Add(i);
        }
        
        a.Sort();
        a.Reverse();
        
        string t = "";
        
        foreach(char j in a)
        {
            t += j;
        }
        
        return Convert.ToInt64(t);
    }
}

/*
public class Solution
{
    public long solution(long n)
    {
        long answer = 0;
        char[] a = n.ToString().ToCharArray();
        System.Array.Sort(a);
        System.Array.Reverse(a);
        answer = System.Convert.ToInt64(new string(a));
        return answer;
    }
}

*/