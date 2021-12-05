// Q231.cs
// https://programmers.co.kr/learn/courses/30/lessons/12930?language=csharp

public class Solution
{
    static char ToUpper(char character)
    {
        char newChar = character;
        if (character > 96 && character < 123)
        {
            newChar = (char)(character - 32);
        }
        return newChar;
    }
    
    static char ToLower(char character)
    {
        char newChar = character;
        if (character > 64 && character < 91)
        {
            newChar = (char)(character + 32);
        }
        return newChar;
    }
    
    public string solution(string s)
    {
        string answer = "";
        int count = 0;
        
        for (int i = 0; i < s.Length; i++)
        {
            count += 1;
            if (s[i] == ' ')
            {
                answer += " ";
                count = 0;
            }
            else if (count % 2 == 1)
                answer += ToUpper(s[i]);
            else
                answer += ToLower(s[i]);
        }
        
        return answer;
    }
}

/*
다른 사람의 풀이
삼항 연산자, ToString 으로 쉽게 해결

public class Solution {
    public string solution(string s) {
        string answer = "";
        int num = 0;

        for(int i = 0; i < s.Length; i++)
        {
            answer += num % 2 == 0 ? s[i].ToString().ToUpper() : s[i].ToString().ToLower();
            num = s[i] == ' '? 0 : num + 1;
        }

        return answer;
    }
}
*/