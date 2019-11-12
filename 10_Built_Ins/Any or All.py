# Enter your code here. Read input from STDIN. Print output to STDOUT

n, array = int(input()), list(map(int, input().split()))

print((all(item > 0 for item in array)) and (any(str(item) == str(item)[::-1] for item in array)))
