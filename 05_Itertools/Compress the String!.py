# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

S = input()

for key, group in groupby(S):
    group_len = len(list(group))
    print("({0}, {1})".format(group_len, key), end=" ")