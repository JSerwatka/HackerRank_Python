# Enter your code here. Read input from STDIN. Print output to STDOUT

_, _ = input().split()
integers = list(input().split())
A = set(input().split())
B = set(input().split())
happines = 0

for i in integers:
    if i in A:
        happines += 1
    elif i in B:
        happines -= 1
    
print(happines)