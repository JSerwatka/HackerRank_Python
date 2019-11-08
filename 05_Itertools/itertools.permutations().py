# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

S, k = input().split()

'''
for element in permutations(sorted(S), int(k)):
    print("".join(element), sep="\n")
'''

print(*["".join(i) for i in permutations(sorted(S), int(k))], sep='\n')