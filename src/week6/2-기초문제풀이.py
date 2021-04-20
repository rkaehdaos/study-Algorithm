# 블랙잭
# https://www.acmicpc.net/problem/2798

import sys

a = list(map(int, sys.stdin.readline().split(' ')))
cards = list(map(int, sys.stdin.readline().split(' ')))

N = a[0]
M = a[1]
result = 0
cards.sort(reverse=True)
result = 0
count = 0
sum = 0
for i in range(N):
    sum = cards[i]
    count = 1
    for j in range(N):
        if i == j or sum + cards[j] > M:
            continue
        else:
            sum += cards[j]
            count += 1
        if count == 3:
            break
    if count == 3 and abs(M - result) > abs(M - sum):
        result = sum
print(result)
