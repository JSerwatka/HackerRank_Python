_ = input()
A = set(input().split())
n = int(input())

for _ in range(n):
    command = input().split()[0]
    update_set = set(input().split())
    getattr(A, command)(update_set)

print(sum(map(int, A)))
