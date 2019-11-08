n = int(input())
s = set(map(int, input().split()))
m = int(input())

for _ in range(m):
    command = list(input().split())
    if len(command) > 1:
        eval("s." + command[0] + "(" + command[1] + ")")
    else:
        eval("s." + command[0] + "()")

print(sum(s))

'''
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))
'''