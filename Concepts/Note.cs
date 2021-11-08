// Note.cs

// 배열
int[] arr1 = new int[5] { 11, 12, 13, 14, 15 };
int[] arr1 = new int[] { 11, 12, 13, 14, 15 }; // index 지정 x

// 다차원 배열
int [ , ] arr1 = new int[2,3] { {31, 32, 33}, {34, 35, 36} };
int [, ,] arr3 = new int[2,3,4];

// 가변 배열
int [][] jaggedArr = new int[3][] 
{
new int[] {31, 32, 33},
new int[] {41, 42, 43, 44, 45, 46, 48, 70, 71, 72, 74, 76},
new int[] {0, 1, 5, 7, 2, 1} 
};
int [][ , ] jaggedArr2 = new int[3][ , ]; // 다차원 가변 배열

// 배열의 길이
// 1차원 배열
Array.Length
ListT.Count // List<T>는 Length가 아니라 Count를 사용

//2차원 배열
Array.GetLength(0)
ListT.Count

// 2차원 배열의 하위 배열 
Array.GetLength(0)
Array.GetLength(1)
ListT.Count
ListT[0].Count

/* 주의 사항
    2차원배열에서의 접근방법은 arr[1, 2]
    가변배열에서의 접근방법은 arr[1][2]
*/

// Nullable
/*
    int?는 32비트 정수 또는 null 값을 보유할 수 있는 형식
    string?은 모든 string 또는 null 값을 보유할 수 있는 형식
*/

// String
string answer = "";
answer.Length // 문자열의 길이