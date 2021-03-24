# 파일 읽고 쓰기
# 파일읽기 : r
# 파일쓰기(기존파일 삭제) : w
# 추가모드(생성 또는 추가) : a

# 파일 읽기
# ex1
# open 이해
f1 = open('./resource/review.txt', 'r')
content1 = f1.read()
print(content1)
print(f1)
print(dir(f1))
f1.close()  # 반드시 사용한 리소스를 반환 필요

print('------------------------------')

# ex2
# open으로 하면  close가 반드시 필요함
# with가 끝나면 자동으로 리소스를 닫아주므로 close 필요없음
with open('./resource/review.txt', 'r') as f2:
    content2 = f2.read()
    print(content2)
    print(list(content2))  # 한글자 리스트형
    print(''.join(list(content2)))  # 리스트를 다시 문자열
    print(iter(content2))  # interator 반환
    print('------------------------------')

    # iterator테스트

print('------------------------------')

# ex3
with open('./resource/review.txt', 'r') as f3:
    for content3 in f3:  # line단위
        # print(content3) # 한줄씩 출력, 컨텐츠의\n때문에 빈줄 생김
        print(content3.strip())  # 양쪽 공백을 제거(줄바꿈도 없어짐)
print('------------------------------')

# ex4
with open('./resource/review.txt', 'r') as f4:
    print('>', f4.read())
    print('>', f4.read())  # 커서가 이미 앞에서 끝까지 갔으므로 빈내용
print('------------------------------')

# ex5
with open('./resource/review.txt', 'r') as f5:
    l5 = f5.readline()  # 한줄 읽어오기
    while l5:  # 값이 없으면 false
        print(l5, end='#### ')
        l5 = f5.readline()
print('------------------------------')

# ex6
# 어차피 iteratable하다면?
with open('./resource/review.txt', 'r') as f6:
    c6 = f6.readlines()
    print(c6)  # 모든 문장을 \n 포함해서 리스트로 가지고 있음
    for c in c6:
        print(c, end=' ***** ') #출력 살펴볼것.. \n뒤로 나와서 *****가 앞으로 출력


# ex 7
with open('./resource/review.txt', 'r') as f7:
    pass


