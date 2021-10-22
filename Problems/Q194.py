# Q194.py
# https://www.hackerrank.com/challenges/one-week-preparation-kit-new-year-chaos/submissions/code/239656649

def minimumBribes(q):
    # Write your code here
    expected = [1, 2, 3]
    count = 0

    for i in range(len(q) - 1):
        if q[i] not in expected:
            print('Too chaotic')
            return
            
        for j in range(3):
            if q[i] == expected[j]:
                count += j
                expected.pop(j)
                expected.append(4 + i)

    print(count)
    return