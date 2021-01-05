from collections import Counter

n = int(input())
words = [input() for _ in range(n)]

counter = Counter(words)
print(len(counter.values()))
print(*counter.values())