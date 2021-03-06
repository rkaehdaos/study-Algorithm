# Excel, csv 읽기 쓰기
# 파이썬 외부 파일 처리
# csv: MIME - text/csv
# ex1

with open('./resource/sample1.csv', 'r') as f:
    print(f.read())

# 파이썬에서 기본으로 제공하는 csv 패키지가 존재
import csv

with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # header부분 skip하고 싶을떄
    print(type(reader))  # 모르면 타입을 찍어본다
    '''클래스 안에 파일내용이 적재가 되어있겠군 '''
    print(dir(reader))  # 어떤 메소드가 있나?
    '''__iter__가 있군 그러면 반복문에서 사용 가능하군'''
    for c in reader:
        print(c)  # 1 row = list 로

# ex2
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')  # 구분자 별도 설정
    next(reader)
    print(type(reader))
    print(dir(reader))

    for c in reader:
        print(c)
# ex3 : Dict 변환 (진짜 편함, 잘 기억할 것)
# 헤더를 key로 전부 key:value상태로 만들 수 있음
# 필요할때 사용하면 정말 도움이 될 듯
with open('./resource/sample1.csv', 'r') as f:
    # reader = csv.reader(f)
    reader = csv.DictReader(f)
    for c in reader:
        print(c)
        for k,v in c.items():
            print(k,v)
        print('----------------')

# ex4 파일쓰기
w=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]
# 처음쓸때 newline에서 \n제거하는 것이 리소스 제거에 효율적
# 10만라인이 20만라인이 되는 것을 막을 수 있음

with open('./resource/sample3.csv','w', newline='') as f:
    #
    wt = csv.writer(f)
    for v in w: # 순회하면서 하기 :특정 조건을 필터링 필요
        print(v)
        wt.writerow(v)  # \n넣어줌


# ex5
with open('./resource/sample4.csv','w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w) # 처리가 필요 없는 경우 한번에 쓸 수 있음


# excel 읽기 XSL, XLSX
# 엑셀을 지원하는 패키지들
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# 주로 pandas 많이 사용(가장 많이 사용하는 openpyxl, xlrd를 내부적으로 사용)
# pip install xlrd
# pip install openpyxl
# pip install pandas
import pandas as pd
# sheetname='시트네임'또는 숫자,header=헤더로 쓸 행, skiprow = 가져오지 않을 행
xlsx = pd.read_excel('./resource/sample.xlsx')
# 상위 데이터 확인 : 첫 5개만 보기
print(xlsx.head())

# 하위 데이터 확인 # 하위 5개
print(xlsx.tail())

# 구조 : 행, 열
print(xlsx.shape)

# excel or csv 다시 쓰기
# index : 첫행에 숫자 넣어주는거
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=True)
