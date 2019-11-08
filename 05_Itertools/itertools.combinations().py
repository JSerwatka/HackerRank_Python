# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations 

S, k = input().split()

for inter in range(1, int(k)+1):
    print(*["".join(comb_elem) for comb_elem in combinations(sorted(S), inter)], sep='\n')
