from collections import deque

d = deque()
N = int(input())

for _ in range(N):
    command, *args = input().split()
    getattr(d, command)(*map(int, args))

print(*d)
