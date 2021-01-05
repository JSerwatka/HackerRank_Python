import itertools
from functools import reduce

curr_list = []
max_reminder = 0
k, M = map(int, input().split())

for _ in range(k):
       curr_list.append(set(map(int, input().split()[1:])))

for elements in itertools.product(*curr_list):
       curr_reminder = sum([x**2 for x in elements]) % M
       max_reminder = curr_reminder if curr_reminder > max_reminder else max_reminder
print(max_reminder)