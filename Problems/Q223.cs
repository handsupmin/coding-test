// Q223.cs
// https://programmers.co.kr/learn/courses/30/lessons/12935

using System.Linq;
using System.Collections.Generic;

public class Solution
{
    public int[] solution(int[] arr)
    {
        if(arr.Length == 1)
        {
            int[] result = {-1};
            return result;
        }
        
        List<int> answer = arr.ToList();
        int min = arr.Min();
        answer.Remove(min);
        
        return answer.ToArray();
    }
}