import sys

n = int(sys.stdin.readline())
print()
print(n, '개')
stack = []
for i in range(1, n):
    stack.append(int(sys.stdin.readline()))

for i in range(n):
    print(i)

print(stack)
