# print : 가장 기본적인 출력 함수
# 작은 따옴, 큰 따옴 다 가능
print('test1')
print("test2")
print("""test2""")
print('''test4''')

print()  # 줄바꿈

## separator 옵션 : 여러 값 join처럼
print('T', 'E', 'S', 'T')
print('T', 'E', 'S', 'T', sep='')
print('2021', '03', '15', sep='-')

## end 옵션 사용 :
print('line1', end='')  # 줄바꿈이 없어짐
print('line2', end='')
print()

## format [] {} ()
print('{} and {}'.format('you', 'me'))  ## 순서대로
print("{0} and {1} and {0}".format('you', 'me'))  ## 매핑 되서 재활용 되는 부분 확인
print('{a} and {b}'.format(a='you', b='me'))  ## 햇갈리지 않게 변수처럼 매핑

## %s: 문자 %d 정수 %f 실수
print("%s's favorite number is %d" % ('seven', 7))  ## 데이터형 까지 정확히 매핑

print("test number : %5d, test price : %4.2f" % (5, 6534.123))  ## 출력부분 확인할 것
print("test number : {0:5d}, test price : {1:4.2f}".format(5, 6534.123))  ## 출력부분 확인할 것
print("test number : {a:5d}, test price : {b:4.2f}".format(a=5, b=6534.123))  ## 출력부분 확인할 것

## Escape Code

'''
Escape Code
\n : 개행
\t : 탭
\\ : 문자 표시
\' : 문자 표시
\" : 문자 표시
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : null문자
'''

print()