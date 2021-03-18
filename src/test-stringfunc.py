# 문자형 관련 연산자
# 슬라이싱이 제일 많이 중요하다고 함

# 복습
str1 = "안근창"
str2 = 'nice man'
str3=''
str4=str()
print (len(str1),len(str2),len(str3),len(str4))

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
str_o1='*'
str_o2='abc'
str_o3='def'
str_o4="Niceman"
print(str_o1*100)
print(str_o2+str_o3)
print('a' in str_o4) # a가 str_o4에 포함되어 있는가?
print('f' in str_o4)
print('z' not in str_o4)