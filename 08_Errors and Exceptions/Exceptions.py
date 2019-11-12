# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except (ZeroDivisionError, ValueError) as error:
        print("Error Code:", error)
