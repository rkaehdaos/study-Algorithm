# 블랙잭
# https://www.acmicpc.net/problem/2798

import sys

a = list(map(int, sys.stdin.readline().split(' ')))
b = list(map(int, sys.stdin.readline().split(' ')))
N = a[0]
M = a[1]
result = 0
print(N, M)
b.sort()
print(b)
# 조합

