# 문자형 관련 연산자
# 슬라이싱이 제일 많이 중요하다고 함

# 복습
str1 = "안근창"
str2 = 'nice man'
str3 = ''
str4 = str()
print(len(str1), len(str2), len(str3), len(str4))

# Raw String : 있는 그대로 표시
# 경로등에 많이 사용
# 이스케이프가 적용되지 않음
raw_s1 = r'c:\Program files\test\Bin'
print(raw_s1)
raw_s2 = r'\\a\\a'
print(raw_s2)

### milti line
multi_test1 = """test multi line"""
print(multi_test1)
multi_test2 = \
    """
    test
     multi
      line
      """
print(multi_test2)

# 문자열 연산
# 문자열 : 불변인 시퀀스
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = "Niceman"
print(str_o1 * 100)
print(str_o2 + str_o3)
print('a' in str_o4)  # a가 str_o4에 포함되어 있는가?
print('f' in str_o4)
print('z' not in str_o4)

## 문자열  현 변환
print(str(77) + 'a')  ## 문자열 +문자열 취급
print(str(10.4))

# 문자열 함수
# https://www.w3schools.com/python/python_ref_string.asp
# 몇개만 테스트

print('a'.islower())
print('testString'.endswith('a'))
print('testString'.endswith('g'))
print('longstring'.capitalize())  # 첫 자만 대문자
print('niceman'.replace('nice', 'good'))

print(reversed('teststring'))
print(list(reversed('teststring')))  # list 형 변환이 필요

t1 = 'teststring'
print(len(t1))
print(t1[0:3])  # 앞숫자부터 뒷 숫자 미만
print(t1[0:len(t1)])  # len을 쓰면 안전하게 가능
print(t1[:4])  # 앞 숫자 없으면 처음부터가 자동으로
print(t1[1:])  # 뒷 수자 없으면 끝까지
print(t1[0:10:2])  # 2개씩 건너뛰며 출력
print(t1[1:-2])  # -인 경우 우측부터
print(t1[-10:-2])
print(t1[::-1])  # 모든것 -1씩 건너뛰며 출력 -> reverse 효과
