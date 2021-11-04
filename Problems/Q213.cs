// Q213.cs
// https://programmers.co.kr/learn/courses/30/lessons/12969?language=csharp

using System;

public class Example
{
    public static void Main()
    {
        String[] s;

        Console.Clear();
        s = Console.ReadLine().Split(' ');

        int a = Int32.Parse(s[0]);
        int b = Int32.Parse(s[1]);
        
        string stars = "";
        
        for (int i = 0; i < b; i++)
        {
            for (int j = 0; j < a; j++)
            {
                stars += "*";
            }
            stars += "\n";
        }

        Console.WriteLine("{0}", stars);
    }
}