_, x = map(int, input().split())

scores = tuple(map(float, input().split()) for _ in range(x))

print(*list(map(lambda y: sum(y) / x, zip(*scores))), sep="\n")
