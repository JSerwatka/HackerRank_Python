A = set(input().split())
n = int(input())
array = []

for _ in range(n):
    array.append(len(set(input().split()) - A) == 0)

print(all(item == True for item in array))