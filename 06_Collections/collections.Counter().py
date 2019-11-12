from collections import Counter

_ = int(input())
shoes_sizes = Counter(list(map(int, input().split())))
money_earned = 0

for _ in range(int(input())):
    desired_shoe = list(map(int, input().split()))
    if shoes_sizes[desired_shoe[0]] > 0:
        money_earned += desired_shoe[1]
        shoes_sizes[desired_shoe[0]] -= 1
    
print(money_earned)
