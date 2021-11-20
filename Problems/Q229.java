// Q229.java
// https://programmers.co.kr/learn/courses/30/lessons/12931?language=java

import java.util.*;

public class Solution
{
    public int solution(int n)
    {
        String strNum = Integer.toString(n);
        int result = 0;
        String[] strArray = strNum.split("");

        for(String s : strArray)
        {
            result += Integer.parseInt(s);
        }
        return result;
    }
}