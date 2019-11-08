# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, input().split())

for i in [x for x in range(1, N) if x % 2 == 1]:
    print((".|."*i).center(M, "-"))

print("WELCOME".center(M,"-"))

for i in [x for x in range(N-1, -1, -1) if x % 2 == 1]:
    print((".|."*i).center(M, "-"))