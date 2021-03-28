# 과제1번 코드란
import csv
with open('./a.csv', 'r') as f:
    print(sum(list(map(int, list(*csv.reader(f)))))) # *을 붙여서 unpacking 가능
