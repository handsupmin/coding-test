// Q227.cs
// https://programmers.co.kr/learn/courses/30/lessons/12932

using System;
using System.Linq;
using System.Collections.Generic;

public class Solution
{
    public int[] solution(long n)
    {
        var data = from c in n.ToString() select int.Parse(c.ToString());
        List<int> numList = data.ToList();
        numList.Reverse();
        int[] numArray = numList.ToArray();
        
        return numArray;
    }
}