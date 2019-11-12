from collections import defaultdict

n, m = map(int, input().split())
a = [input() for _ in range(n)]
b_items = [input() for _ in range(m)]

b = defaultdict(list)

for i in range(n):
    b[a[i]].append(i + 1)

for item in b_items:
    if item not in b:
        print("-1")
    else:
        print(*b[item])
