# 블랙잭
# https://www.acmicpc.net/problem/2798

import sys

N, M = list(map(int, sys.stdin.readline().split(' ')))
cards = list(map(int, sys.stdin.readline().split(' ')))
result = 0
count = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            sumValue = cards[i] + cards[j] + cards[k]
            if sumValue <= M:
                result = max(result, sumValue)
print(result)
