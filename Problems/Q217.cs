// Q217.cs
// https://programmers.co.kr/learn/courses/30/lessons/12948?language=csharp

public class Solution {
    public string solution(string phone_number) {
        string answer = "";
        
        for(int i = 0; i < phone_number.Length; i ++)
        {            
            if (i >= (phone_number.Length - 4))
                answer += phone_number[i];
            else
                answer += "*";            
        }
        
        return answer;
    }
}