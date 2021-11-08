// Q216.cs
// https://www.acmicpc.net/submit/1000/35180852

using System;

namespace baekjoon
{
    class Solve
    {
        static void Main(string[] args)
        {
            string input = Console.ReadLine();
            string[] arr_input = input.Split();

            Console.WriteLine(int.Parse(arr_input[0])+ int.Parse(arr_input[1]));
        }
    }
}