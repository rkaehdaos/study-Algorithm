# h2
'''
두 문자열 A와 B가 있을 때, 두 문자열의 '최대공약문자열' C를 아래와 같이 정의하자.

문자열 C를 반복하여 문자열 A와 B를 생성할 수 있다.
가능한 C 중에 가장 긴 문자열을 C로 한다.
위 조건을 만족하는 C가 없으면 빈 문자열을 C로 한다.
이 때, 문자열 A와 B를 입력받아 C를 출력하는 프로그램을 작성하시오.
'''

def gcdString(A, B):
    len_t = len(A)
    len_c = len(B)
    result = ''
    for i in range(len_t):
        for j in range(len_c):
            lcs_temp = 0
            match = ''
            while ((i + lcs_temp < len_t) and (j + lcs_temp < len_c) and (A[i + lcs_temp] == B[j + lcs_temp])):
                match += B[j + lcs_temp]
                lcs_temp += 1
            if len(match) > len(result):
                result = match
    print(result)


gcdString('ababcde', 'ababcde')  # 'ababcde'
gcdString('ababababab', 'abab')  # 'ab'
gcdString('abababab', 'abab')  # 'abab'
gcdString('fast', 'campus')  # ''
