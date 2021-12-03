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
Array.Length;
ListT.Count; // List<T>는 Length가 아니라 Count를 사용

//2차원 배열
Array.GetLength(0);
ListT.Count;

// 2차원 배열의 하위 배열 
Array.GetLength(0);
Array.GetLength(1);
ListT.Count;
ListT[0].Count;

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
answer.Length; // 문자열의 길이

// Convert.ToInt32 vs Int32.Parse vs Int32.TryParse
// 테스트를 위한 string 변수 생성 및 다양한 값 할당
string a = "123";
string b = "0.1";
string c = null;
// Convert.ToInt32
Convert.ToInt32(a); // 123
Convert.ToInt32(b); // FormatException
Convert.ToInt32(c); // 0
// Int32.Parse
Int32.Parse(a); // 123
Int32.Parse(b); // FormatException
Int32.Parse(c); // ArgumentNullException
// Int32.TryParse
int i;
Int32.TryParse(a, out i); // true (123)
Int32.TryParse(b, out i); // false (0)
Int32.TryParse(c, out i); // false (0)
// Convert 와 Parse의 차이는 파라미터가 null 일때 0을 반환하는지, 예외처리를 해주는지의 차이이다.
// 상황에 맞게 사용해야 하지만 가급적이면 안전하게 사용하기 위해서 자체 예외 핸들링을 해주는 TryParse 를 쓰도록 하자.

// 배열의 평균
using System.Linq;
Array.Average();

// 삼항연산자
int number = 2;
bool isEven;
// condition ? consequent : alternative
isEven = (number % 2 == 0) ? true : false ;

/*
char과 string은 int로 변환했을 때, 다르다.
char -> string -> int
char Character = '9';
int integer = int.Parse(Character.ToString());
*/

// 배열 <-> 리스트 변환
using System.Linq;
List<int> testList = testArr.ToList();
int[] testArray = testList.ToArray();

// char[] <-> string
char[] a = n.ToString().ToCharArray();
System.Convert.ToInt64(new string(a));

// long -> char[] -> Array
long n = 123454536
char[] a = n.ToString().ToCharArray();
// Array -> string -> long
System.Convert.ToInt64(new string(a));