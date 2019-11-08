n = int(input())

print(len(set(input() for _ in range(n))))

''' 
wersja z uzyciem .add
stamps_set = set()

for _ in range(n):
    stamps_set.add(input())

print(len(stamps_set))
'''